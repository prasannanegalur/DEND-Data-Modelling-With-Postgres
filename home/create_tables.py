import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    '''
    This function creates the sparkifydb in the postgres server by connecting to student database
    It returns a tuple with connection object and cursor object
    Sample call to the function: 
    cur, conn = create_database()
    '''
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    '''
    This function drops the tables in the sparkifydb database
    It expects the cursor and connection objects to the students database
    It doesn't return anything
    Sample call to the function: 
    drop_tables(cur, conn)
    '''
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
    This function creates the tables in the sparkifydb database
    It expects the cursor and connection objects to the students database
    It doesn't return anything
    Sample call to the function: 
    create_tables(cur, conn)
    '''

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    # below line is commented as it is not required. The create_database() function drops and creates the sparkify database, dropping all the tables
    #drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()