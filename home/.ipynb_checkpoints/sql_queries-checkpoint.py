# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE users"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
songplay_id SERIAL PRIMARY KEY, 
start_time timestamp, 
user_id int, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id int, 
location varchar, 
user_agent varchar
)
""")

user_table_create = ("""
CREATE TABLE users (
user_id int PRIMARY KEY, 
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar
)
""")

song_table_create = ("""
CREATE TABLE songs (
song_id varchar PRIMARY KEY, 
title varchar, 
artist_id varchar, 
year int, 
duration decimal
)
""")

artist_table_create = ("""
CREATE TABLE artists (
artist_id varchar PRIMARY KEY, 
name varchar, 
location varchar, 
latitude decimal, 
longitude decimal
)
""")

time_table_create = ("""
CREATE TABLE time (
start_time timestamp PRIMARY KEY, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users VALUES (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level = EXCLUDED.level 
""")

song_table_insert = ("""
INSERT INTO songs VALUES (%s, %s, %s, %s, %s) ON CONFLICT(song_id) DO UPDATE SET title = EXCLUDED.title 
""")

artist_table_insert = ("""
INSERT INTO artists VALUES (%s, %s, %s, %s, %s) ON CONFLICT(artist_id) DO UPDATE SET location = EXCLUDED.location
""")


time_table_insert = ("""
INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT(start_time) DO UPDATE SET month = EXCLUDED.month
""")

# FIND SONGS

song_select = ("""
SELECT
s.song_id,
a.artist_id
FROM songs s
INNER JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s
AND a.name = %s
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]