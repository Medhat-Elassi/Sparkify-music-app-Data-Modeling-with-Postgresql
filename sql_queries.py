# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = (""" create table songplays(
songplay_id serial primary key,
start_time timestamp not null,
user_id int not null,
level varchar not null,
song_id varchar,
artist_id varchar,
session_id int not null,
location varchar not null,
user_agent varchar not null
)
""")

user_table_create = ("""
create table users(
user_id int primary key,
first_name varchar not null,
last_name varchar not null,
gender char(1) not null,
level varchar not null
)
""")

song_table_create = ("""
create table songs(
song_id varchar primary key,
title varchar not null,
artist_id varchar not null,
year int not null,
duration float not null
)
""")

artist_table_create = ("""
create table artists(
artist_id varchar primary key,
artist_name varchar not null,
artist_location varchar not null,
artist_latitude DOUBLE PRECISION,
artist_longitude DOUBLE PRECISION
)
""")

time_table_create = ("""
create table time(
start_time timestamp primary key,
hour int not null,
day int not null,
week int not null,
month int not null,
year int not null,
weekday int not null
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    values(%s,%s,%s,%s,%s,%s,%s,%s)
    on conflict do nothing
""")

user_table_insert = ("""
insert into users
    (user_id, first_name, last_name, gender, level)
    values(%s,%s,%s,%s,%s)
    on conflict(user_id) do
    update
    set level = excluded.level 
""")

song_table_insert = ("""
insert into songs
    (song_id, title, artist_id, year, duration)
    values(%s,%s,%s,%s,%s)
    on conflict do nothing
""")

artist_table_insert = ("""
insert into artists
    (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    values(%s,%s,%s,%s,%s)
    on conflict do nothing
""")


time_table_insert = ("""
insert into time
    (start_time, hour, day, week, month, year, weekday)
    values(%s,%s,%s,%s,%s,%s,%s)
    on conflict do nothing
""")

# FIND SONGS

song_select = ("""
select songs.song_id, artists.artist_id
from songs join artists
on songs.artist_id = artists.artist_id
where songs.title=%s
and
artists.artist_name=%s
and
songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]