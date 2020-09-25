# Udacity Data Engineering: Sparkify Project

- Data modeling with Postgres and building an ETL pipeline using Python. 


## Introduction

Sparkify is a music company that needs analysis on song and user activity for their new music streaming app. To help analytics team understand what songs their users listen to, I've set up a Postgres database, schema, and ETL pipeline with tables designed to optimize running queries on song plays. Further, I've created a pipeline that easily transfers files from repositories to go directly into Posgres.

There were two datasets: song information from the Million Song Dataset and generated user data that tracks interaction with music. Files were stored in the JSON format and contains song details, artist details, and user play details.


## Schema
The schema is 5 tables. The information for songs and artists table came from the 
song_data file. The log_data folder contains information for the time table and the users table. For the time table, the information is extracted from one column containing the timestamp for user plays. The songplay table 
The time table comes from log The information for the songplay table comes from the other 4 tables. A SQL query was written to get song_id and artist_id for songs that were in the song_data file, the songs with no matches simply have NONE value. 

### Entity Relationship Diagram

<img width="781" alt="Table Schema" src="https://user-images.githubusercontent.com/53429726/94280085-fd2c6880-ff1a-11ea-86e8-8e62dbc5ea1b.png">



## ETL pipeline

Processing the data for the `songs` and `artists` dimension tables came directly from the song_data folder. Each JSON file contained one row containing information for one song with the corresponding artist information. 

Songs and Artists:
- Open the song_data files using the get_files() function and save into a DataFrame
- Choose relevent columns (for songs and artists table) and save into its own DataFrame
- Loop through each row in (songs or artist DataFrame) and insert values into (songs or artists table)

Time:
- Open the log_data files using the get_files() function and save into a DataFrame
- Reset index of DataFrame as each JSON file has multiple rows of information on users
- Filter the DataFrame so we only have information where the 'page' is named 'NextSong'
- Isolate the time column ('ts') and turn string into a datetime format with 'ms' setting (milliseconds)
- Create a new DataFrame from extracted time values from the datetime column
- Loop through each row and insert into time table

Users:
- Same as songs and artist steps

Songplays:
- create a sql query to find the artist_id and song_id using a given artist_name and song.title.
- from the DataFrame created using the log_data files, go through each row and try to match the artist name and song name to an artist in the artists table or song in the songs table
- if found, save the song_id and artist_id to a variable, otherwise set variables to NONE
- insert all the relevant columns and the crated song_id and artist_id variables to the songplay table


## Example Queries
After completing the project, all of the queries pass the tests from the provided `tests.ipynb`. There are a lot of NONE values for song_id and artist_id in the songplay table because there are only 73 songs in the song_data file. It turns out just one song is in both the song_data and log_data.

<img width="972" alt="Screen Shot 2020-07-17 at 4 45 02 PM" src="https://user-images.githubusercontent.com/53429726/94287591-8005f100-ff24-11ea-864e-0488d1f50693.png)">


## Conclusion
The project provided a good way to practice creating a database and creating an ETL pipeline to insert raw data files to our finished tables.