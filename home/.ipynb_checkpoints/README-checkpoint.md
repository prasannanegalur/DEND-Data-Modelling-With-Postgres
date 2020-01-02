## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.

Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project Description
The purpose of the project is to provide analytical capability on the data to arrive at answers for various business questions. The data will be split into fact and dimension tables on a Postgres database to optimize queries on song play analysis.

## Datasets

### Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. 

For example, below are the filepaths to two files in this dataset.

song_data/A/B/C/TRABCEI128F424C983.json

song_data/A/A/B/TRAABJL12903CDCF1A.json

Below is an example of a single song file - 

{
   "num_songs": 1,
   "artist_id": "ARD7TVE1187B99BFB1",
   "artist_latitude": null,
   "artist_longitude": null,
   "artist_location": "California - LA",
   "artist_name": "Casual",
   "song_id": "SOMZWCG12A8C13C480",
   "title": "I Didn't Mean To",
   "duration": 218.9318,
   "year": 0
}


### Log Dataset
The second dataset consists of log files in JSON format.

The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.

log_data/2018/11/2018-11-12-events.json

log_data/2018/11/2018-11-13-events.json


And below is an example in a log file - 

{
   "artist": null,
   "auth": "Logged In",
   "firstName": "Walter",
   "gender": "M",
   "itemInSession": 0,
   "lastName": "Frye",
   "length": null,
   "level": "free",
   "location": "San Francisco-Oakland-Hayward, CA",
   "method": "GET",
   "page": "Home",
   "registration": 1.54091913E12,
   "sessionId": 38,
   "song": null,
   "status": 200,
   "ts": 1541105830796,
   "userAgent": "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
   "userId": "39"
}

The data from these files are extracted and loaded in to the corresponding dimension and fact tables using python and postgres SQL.

## Code Details

Below are the tables design for the the project - 

### Dimension Tables
**users** - users in the app
columns: user_id, first_name, last_name, gender, level

**songs** - songs in music database
columns: song_id, title, artist_id, year, duration

**artists** - artists in music database
columns: artist_id, name, location, latitude, longitude

**time** - timestamps of records in songplays broken down into specific units
columns: start_time, hour, day, week, month, year, weekday

### Fact Table

**songplays** - records in log data associated with song plays i.e. records with page NextSong
columns: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

The project repository has below files:

### main files
sql_queries.py -- This script contains the strings with SQL statemtements for each table (CREATE TABLE/INSERT STATEMENTS), etc..

create_tables.py -- This script contains functions to drop and create the sparkify database and the tables 

etl.py -- This script contains the functions to perform various ETL pipelines. Process the songs files and log files and load the corresponding dimenstion and fact tables

### work files
etl.ipynb -- jupyter notebook has individual python commands with debugging steps

test.ipynb -- jupyter notebook has sql commands to verify the data is loaded properly in the tabbles

Untitled.ipynb -- jupyter notebook has commands to run the scripts 


### steps to run the project
1. Run the create_tables.py to create the databases and tables

!python create_tables.py (when running through jupyter notebook)

python create_tables.py (when running through commnd line)

2. Run the etl.py to create load the tables

!python etl.py (when running through jupyter notebook)

python etl.py (when running through commnd line)


### Sample analysis that will be possible with this schema

***No. of mins of songs played by each customer***

select 
u.first_name,
u.last_name,
sum(s.duration) duration
from songplays sp
inner join users u on sp.user_id = u.user_id
inner join songs s on sp.song_id = s.song_id
group by u.first_name,
u.last_name


***Paid customers ratio***

select 
sum(case when level = 'paid' then 1 else 0 end)/count(distinct user_id) MonetizableUsersRatio
from songplays sp

