# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES


songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays ( songplay_id serial, \
                            start_time timestamp NOT NULL, \
                            user_id int REFERENCES users(user_id), \
                            level varchar, \
                            song_id varchar REFERENCES songs(song_id), \
                            artist_id varchar REFERENCES artists(artist_id), \
                            session_id int, \
                            location varchar, \
                            user_agent varchar, \
                            CONSTRAINT songplays_pk PRIMARY KEY(songplay_id))""")



user_table_create = ("""CREATE TABLE IF NOT EXISTS users ( user_id int, \
                        first_name varchar, last_name varchar, \
                        gender varchar, level varchar, \
                        CONSTRAINT users_pk PRIMARY KEY(user_id) ) """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs ( song_id varchar, \
                        title varchar, \
                        artist_id varchar NOT NULL, \
                        year int, \
                        duration real, CONSTRAINT songs_pk PRIMARY KEY(song_id)) \
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists ( artist_id varchar, \
                          name varchar, location varchar, \
                          latitude real, longitude real, \
                          CONSTRAINT artists_pk PRIMARY KEY(artist_id) ) """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time ( start_time timestamp, \
                        hour int, day int, week int, month int, \
                        year int, weekday int, \
                        CONSTRAINT time_pk PRIMARY KEY(start_time)) """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s ) \
                        ON CONFLICT ON CONSTRAINT songplays_pk \
                        DO NOTHING \
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                        VALUES (%s, %s, %s, %s, %s ) \
                        ON CONFLICT ON CONSTRAINT users_pk \
                        DO \
                        UPDATE SET level = EXCLUDED.level \
""") 

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) \
                        VALUES (%s, %s, %s, %s, %s) \
                        ON CONFLICT ON CONSTRAINT songs_pk \
                        DO NOTHING \
""")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude , longitude) \
                        VALUES (%s, %s, %s, %s, %s) \
                        ON CONFLICT ON CONSTRAINT artists_pk \
                        DO NOTHING \
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day,  week, month, year , weekday) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s ) \
                        ON CONFLICT ON CONSTRAINT time_pk \
                        DO NOTHING \
""")

# FIND SONGS

song_select = ("""SELECT song_id, songs.artist_id FROM \
                  songs INNER JOIN artists \
                  ON songs.artist_id = artists.artist_id                  
                  WHERE \
                  songs.title = %s \
                  AND \
                  artists.name = %s \
                  AND \
                  songs.duration = %s           
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]