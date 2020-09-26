import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    - Opens song data file
    - Insert song record
    - Insert artist record
    """
    # open song file
    df = pd.read_json(filepath, lines = True)
    
    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    - opens log file
    - filter by NextSong page
    - convert timestamp to datetime from string
    - insert time data 
    - insert user table
    - insert songplay records 
    """
    # open log file
    df = pd.read_jason(filepath, lines = True)

    # filter by NextSong action
    df = df[df.page == 'NextSong']
    df = df.reset_index()

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')
    
    # insert time data records
    time_data = [df.ts.dt.time, df.ts.dt.hour,df.ts.dt.day, df.ts.dt.weekofyear,df.ts.dt.month,df.ts.dt.year, df.ts.dt.weekday]
    column_labels = ['time', 'hour', 'day', 'weekofyear', 'month', 'year', 'weekday']
    time_df = pd.DataFrame()
    for i in range(len(column_labels)):
        time_df[column_labels[i]] = time_data[i]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df['userId', 'firstName', 'lastName', 'gender', 'level']

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.artist, row.song))
        if cur.fetchone():
            #have to rerun because we can only use statement once
            cur.execute(song_select, (row.artist, row.song))
            #save into variables
            songid, artistid = cur.fetchone()
        else: 
            #save none into variables
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, int(row.userId), row.level, songid, artistid, int(row.sessionId), row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    - Get all files matching extension from directory
    - Get total number of files found
    - iterate over files and process
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    - creates connection to database
    - returns connection and cursor
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()