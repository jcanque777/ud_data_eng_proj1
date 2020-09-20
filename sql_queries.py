# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

'''
CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time time, user_id int, level VARCHAR, \
artist_id varchar, session_id int, location VARCHAR, user_Agent VARCHAR)

'''


songplay_table_create = ('CREATE TABLE IF NOT EXISTS songplay (songplay_id int, \
start_time time, \
user_id int, \
level VARCHAR, \
artist_id varchar, \
session_id int, \
location VARCHAR, \
user_Agent VARCHAR);')


'''
CREATE TABLE IF NOT EXISTS users (user_id int, \
first_name VARCHAR, \
last_name VARCHAR, \
gender VARCHAR, \
level VARCHAR);
'''


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, \
first_name VARCHAR, \
last_name VARCHAR, \
gender VARCHAR, \
level VARCHAR);""")


'''
CREATE TABLE IF EXISTS songs (song_id VARCHAR, \
title VARCHAR, \
artist_id VARCHAR, \
year int, \
duration numeric;
'''

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR, \
title VARCHAR, \
artist_id VARCHAR, \
year int, \
duration numeric);""")


''' 
CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR, \
artist_name VARCHAR, \
artist_location VARCHAR, \
artist_latitude numeric, \
aritst_longitude numeric);
'''

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR, \
artist_name VARCHAR, \
artist_location VARCHAR, \
artist_latitude numeric, \
aritst_longitude numeric);""")


"""
CREATE TABLE IF NOT EXISTS time (start_time INT PRIMARY KEY, \
hour int, \
day int, \
week int, \
month int, \
year int, \
weekday int);
"""


time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time INT PRIMARY KEY, \
hour int, \
day int, \
week int, \
month int, \
year int, \
weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")



user_table_insert = ("""
""")


song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration), \
VALUES (%s, %s, %s, %s, %s) ON CONFLICT ON CONSTRAINT song_table_pkey DO NOTHING""")


artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]