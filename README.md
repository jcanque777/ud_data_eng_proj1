# Udacity Data Engineering: Sparkify Project

- Data modeling with Postgres and building an ETL pipeline using Python. 


## Introduction

Sparkify is a music company that needs analysis on song and user activity for their new music streaming app. To help analytics team understand what songs their users listen to, I've set up a Postgres database, schema, and ETL pipeline with tables designed to optimize running queries on song plays. Further, I've created a pipeline that easily transfers files from repositories to go directly into Posgres.

There were two datasets: song information from the Million Song Dataset and generated user data that tracks interaction with music. Files were stored in the JSON format and contains song details, artist details, and user play details.


## Schema
The schema is 5 table with: songs, artist,


### Entity Relationship Diagram

<img width="781" alt="Table Schema" src="https://user-images.githubusercontent.com/53429726/94280085-fd2c6880-ff1a-11ea-86e8-8e62dbc5ea1b.png">



## ETL pipeline

Processing the data for the `songs` and `artists` dimension tables was fairly straightforward as each JSON file only contained information for one song. The steps for processing the "song" data were:
- Open the file
- Set the column names *(note: because I read the JSON file as a series, I set the index instead of column names)*
- Insert appropriate `songs_table` values
- Insert appropriate `artists_table` values


While the `users` table  was painless to create, processing the data for the `time`, `users`, and `songplays` tables was less straightforward as each JSON file was a simulated activity log for a single day.  The orginal time data was provided in milliseconds, so that was converted to a timestamp and processed to insert `start_time`, `hour`, `day`, `week`, `month`, `year`, and `weekday` values into the `time` table. The `songplays` table contains the values for `timestamp`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, and `user_agent`. Because the log files do not specify an ID for either the song or the artist, it was necessary to first query the songs and artists tables to find matches based on song title, artist name, and song duration time.


The steps for processing the "log" data were:
- Open the file and filter by `NextSong` attribute
- Convert timestamp, process, and insert `time` data
- Insert appropriate `users` tables values
- Iteratively execute query to match `song_id` and `artist_id` for `songplays` table data
- Insert appropriate `songplays` tables values



## Example Queries
After completing the project, all of the queries pass the tests from the provided `tests.ipynb`. Below, I have provided three example queries. There is only one song from the songs data that matches up with the log data, so I chose that song to use for the examples:

<img width="972" alt="Screen Shot 2020-07-17 at 4 45 02 PM" src="https://user-images.githubusercontent.com/34200538/87829358-ef88a180-c84c-11ea-808f-9f1eebdf306b.png">


## Conclusion
This project was a great learning experience. I was able to strengthen my data modeling and ETL pipeline building skills while getting aa solid introduction to Postgres SQL. 