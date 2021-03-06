import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):    
    """Get the information of a song file under the provided filepath \
       and insert this information into PostgreSQL tables.
    
    Parameters:
        cur (psycopg2.cursor()): cursor of the sparkifydb database 
        filepath (string): a string containing the file path containing the song files. 
    
    Returns: 
        Nothing, the function simply performs data processing            
    """ 
        
    df = pd.read_json(filepath, lines=True)

    song_data = list(df[["song_id", "title", "artist_id", "year", "duration"]].iloc[0,:].values)
    
    song_data[3] = song_data[3].item()
    song_data[4] = song_data[4].item()
    
    try:
        cur.execute(song_table_insert, song_data)
    except Exception as error:
        print("Oops! An exception has occured:", error)
        print("Exception TYPE:", type(error))
    
    artist_data = list(df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].iloc[0,:].values)
    
    try:
        cur.execute(artist_table_insert, artist_data)
    except Exception as error:
        print("Oops! An exception has occured:", error)
        print("Exception TYPE:", type(error))        
        

def process_log_file(cur, filepath):
    """Get the information of a log file under the provided filepath \
       and insert this information into PostgreSQL tables.
    
    Parameters:
        cur (psycopg2.cursor()): cursor of the sparkifydb database 
        filepath (string): a string containing the file path containing the log files. 
    
    Returns: 
        Nothing, the function simply performs data processing            
    """ 
    
    df = pd.read_json(filepath, lines=True)

    df = df[df["page"] == 'NextSong']

    df["ts"] = pd.to_datetime(df["ts"], unit='ms')
    t = df["ts"]

    time_data = (t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ("timestamp", "hour", "day", "weekofyear", "month", "year", "weekday")
    
    dict_data = dict(zip(column_labels, time_data))
    
    time_df = pd.DataFrame.from_dict(dict_data)

    for i, row in time_df.iterrows():
        try:
            cur.execute(time_table_insert, list(row))
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))        
                    

    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    for i, row in user_df.iterrows():
        try:
            cur.execute(user_table_insert, row)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))        
            
        

    for index, row in df.iterrows():      
        
        try:
            cur.execute(song_select, (row.song, row.artist, row.length))
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))        
            continue 
            
            
        try:
            results = cur.fetchone()
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))        
            continue 
            
            
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        
        try:
            cur.execute(songplay_table_insert, songplay_data)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            continue
            
            


def process_data(cur, conn, filepath, func):
    """Process the information of song or log files under the provided filepath \
       and insert this information into PostgreSQL tables.
    
    Parameters:
        cur (psycopg2.cursor()): cursor of the sparkifydb database 
        filepath (string): a string containing the file path containing \
                           the song or log files. 
        func (function): the python function to be used to process the song or log files
    
    Returns: 
        None, the function simply performs data processing            
    """     
    
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()