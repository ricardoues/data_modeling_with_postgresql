import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """Create the sparkify database.
    
    Parameters:
        Nothing, this function does not have parameters. 
    
    Returns: 
        cur, conn: cursor and connection to the sparkify database.            
    """ 
        
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    
    conn.close()    
        
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """Drop the tables of the sparkify database.
    
    Parameters:        
        cur (psycopg2.cursor()): cursor of the sparkifydb database 
        conn (psycopg2.connect()): the connection to the sparkifydb database. 

    
    Returns: 
        None, the function simply drops the tables of the sparkify database.            
    """ 
    
        
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Create the tables of the sparkify database.
    
    Parameters:        
        cur (psycopg2.cursor()): cursor of the sparkifydb database 
        conn (psycopg2.connect()): the connection to the sparkifydb database. 

    
    Returns: 
        None, the function simply create the tables of the sparkify database.            
    """ 
        
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)    

    conn.close()


if __name__ == "__main__":
    main()