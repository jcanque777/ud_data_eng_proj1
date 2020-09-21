# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES


songplay_table_create = ('CREATE TABLE IF NOT EXISTS songplay (songplay_id INT PRIMARY KEY, \
start_time time NOT NULL, \
user_id INT NOT NULL, \
level VARCHAR, \
artist_id VARCHAR, \
session_id INT, \
location VARCHAR, \
user_agent VARCHAR);')


user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, \
first_name VARCHAR NOT NULL, \
last_name VARCHAR NOT NULL, \
gender VARCHAR, \
level VARCHAR);""")



song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY, \
title VARCHAR NOT NULL, \
artist_id VARCHAR NOT NULL, \
year INT, \
duration NUMERIC NOT NULL);""")


artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, \
artist_name VARCHAR NOT NULL, \
artist_location VARCHAR, \
artist_latitude NUMERIC, \
artist_longitude NUMERIC);""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time BIGINT PRIMARY KEY, \
hour INT NOT NULL, \
day INT NOT NULL, \
week INT NOT NULL, \
month INT NOT NULL, \
year INT NOT NULL, \
weekday INT NOT NULL);
""")

# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songs (song_id, \
title, artist_id, year, duration), \
VALUES (%s, %s, %s, %s, %s);""")


user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level), \
VALUES (%s, %s, %s, %s, %s), \
ON CONFLICT ON CONSTRAINT users_table_pkey, \
DO UPDATE SET level=EXCLUDED.level;""")


song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration), \
VALUES (%s, %s, %s, %s, %s), \
ON CONFLICT ON CONSTRAINT,\
songs_table_pkey DO NOTHING;""")


artist_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude), \
VALUES (%s, %s, %s, %s, %s), \
ON CONFLICT ON CONSTRAINT, \
artist_table_pkey DO NOTHING;""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday), \
VALUES (%s, %s, %s, %s, %s, %s, %s), \
ON CONFLICT ON CONSTRAINT, \
time_table_pkey DO NOTHING;""")


# FIND SONGS

song_select = ("""SELECT a.artist_id, s.song_id
FROM artists a
INNER JOIN songs s
ON s.artist_id = a.artist_id
WHERE a.name = %s
AND s.title = %s
AND s.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]