# DROP TABLES

music_by_sessionId_drop = "DROP TABLE IF EXISTS music_by_sessionId"
music_by_userId_drop = "DROP TABLE IF EXISTS music_by_userId"
music_by_song_drop = "DROP TABLE IF EXISTS music_by_song"

# CREATE TABLES

music_by_sessionId_create = '''CREATE TABLE IF NOT EXISTS music_by_sessionId
                              (sessionId int,
                              itemInSession int,
                              userId int,
                              firstName text,
                              lastName text,
                              user text,
                              gender text,
                              length float,
                              level text,
                              location text,
                              song text,
                              artist text,
                              PRIMARY KEY (sessionId, itemInSession))
'''

music_by_userId_create = '''CREATE TABLE IF NOT EXISTS music_by_userId
                              (userId int,
                              sessionId int,
                              itemInSession int,
                              firstName text,
                              lastName text,
                              user text,
                              gender text,
                              length float,
                              level text,
                              location text,
                              song text,
                              artist text,
                              PRIMARY KEY ((userId, sessionId), itemInSession))
'''

music_by_song_create = '''CREATE TABLE IF NOT EXISTS music_by_song
                           (song text,
                            sessionId int,
                            userId int,
                            firstName text,
                            lastName text,
                            user text,
                            gender text,
                            itemInSession int,
                            length float,
                            level text,
                            location text,
                            artist text,
                            PRIMARY KEY (song, userId))
'''

# INSERT QUERIES
music_by_sessionId_insert = '''INSERT INTO music_by_sessionId
                              (sessionId, itemInSession, userId, firstName, lastName, user, gender, length, level, location, song, artist)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

music_by_userId_insert = '''INSERT INTO music_by_userId
                            (userId, sessionId, itemInSession, firstName, lastName, user, gender, length, level, location, song, artist)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

music_by_song_insert = '''INSERT INTO music_by_song
                          (song, userId, sessionId, itemInSession, firstName, lastName, user, gender, length, level, location, artist)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# QUERY LISTS/DICTIONARIES

create_table_queries =  [music_by_sessionId_create, music_by_song_create, music_by_userId_create]

insert_queries = {'music_by_sessionId': music_by_sessionId_insert,
                  'music_by_userId': music_by_userId_insert,
                  'music_by_song': music_by_song_insert
}
drop_table_queries = [music_by_sessionId_drop, music_by_song_drop, music_by_userId_drop]