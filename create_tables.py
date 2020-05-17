import cassandra
from queries import create_table_queries, insert_queries, drop_table_queries
import csv

def create_keyspace():
    """
    - Creates and connects to the sparkify
    - Returns the session
    """
    from cassandra.cluster import Cluster
    cluster = Cluster()

    # To establish connection and begin executing queries, need a session
    session = cluster.connect()
    
    # Create Keyspace
    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS sparkify 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
        )

    except Exception as e:
        print(e)
    
    # Set Keyspace
    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)
        
    return session, cluster

def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        session.execute(query)
        
def create_tables(session):
    """
    Creates each table and loads the data using the queries in `create_table_queries` dictionary. 
    """
    print("Creating tables")
    for query in create_table_queries:
        session.execute(query)
    print(f"Finished.\n")
    
    print("Loading music_by_sessionId Data...")
    load_music_by_sessionId_data(session)
    print(f"Finished.\n")
    
    print("Loading music_by_userId Data...")
    load_music_by_userId_data(session)
    print(f"Finished.\n")
    
    print("Loading music_by_song Data...")
    load_music_by_song_data(session)
    print(f"Finished.\n")

def load_music_by_sessionId_data(session, file='event_datafile_new.csv'):
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            userId, firstName, lastName, user, gender, itemInSession, length, level, location, sessionId, song, artist = int(line[10]), line[1], line[4], f"{line[1]} {line[4]}", line[2], int(line[3]), float(line[5]), line[6], line[7], int(line[8]), line[9], line[0]
        
            query = insert_queries['music_by_sessionId']
            session.execute(query, (sessionId, itemInSession, userId, firstName, lastName,
                                    user, gender, length, level, location, song, artist))
            
def load_music_by_userId_data(session, file='event_datafile_new.csv'):
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            userId, firstName, lastName, user, gender, itemInSession, length, level, location, sessionId, song, artist = int(line[10]), line[1], line[4], f"{line[1]} {line[4]}", line[2], int(line[3]), float(line[5]), line[6], line[7], int(line[8]), line[9], line[0]
        
            query = insert_queries['music_by_userId']
            session.execute(query, (userId, sessionId, itemInSession, firstName, lastName,
                                    user, gender, length, level, location, song, artist))
            
def load_music_by_song_data(session, file='event_datafile_new.csv'):
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
            userId, firstName, lastName, user, gender, itemInSession, length, level, location, sessionId, song, artist = int(line[10]), line[1], line[4], f"{line[1]} {line[4]}", line[2], int(line[3]), float(line[5]), line[6], line[7], int(line[8]), line[9], line[0]
        
            query = insert_queries['music_by_song']
            session.execute(query, (song, userId, sessionId, itemInSession, firstName,
                                    lastName, user, gender, length, level, location, artist))
            
def main():
    """
   - Drops (if exists) and Creates the sparkify keyspace. 
    
   - Establishes connection with the sparkify keyspace.  
    
   - Drops all the tables.  
    
   - Creates and loads all tables needed. 
    
   - Finally, closes the connection.
    """ 
    session, cluster = create_keyspace()
    
    drop_tables(session)
    create_tables(session)
   
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()