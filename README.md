Sparkify Apache Cassandra Database
==================================

Sparkify (a startup) collects data on songs and user activity on their new music streaming app. We were particularly interested in understanding what songs users are listening to. This task was difficult as the data reside in a directory of CSV files on user activity on the app.

This ETL pipeline processes the data from the CSV files and loads them into a Apache Cassandra database. 

Database Tables
===============

All tables contained all dataset columns but they are partitioned and clustered depending on the query. While I initially chose to reduce the columns in each table, I later preferred to keep the full dataset so that the analyst running a specific query can have as much information on a row as available.  

1. **music_by_sessionId**: This table partitions the data by **sessionId** and clusters by **itemInSession**
    - This table is modeled after:  **Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4**.


2. **music_by_userId**: This table partitions the data by **userId**, **sessionId** and clusters by, **itemInSession**
    - This table is modeled after: **Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182**.


3. **music_by_song**: This table partitions the data by **song**, **userId** composite key to ensure it is unique and avoid duplication of data (since we don't care if a person has listened to the same song several times in this query).
    - This table is modeled after: **Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'**. 
    
    
How to Run
=====================

Simply run the **run.sh** on a unix command line. It will preprocess the CSV files, reset the tables and loads the data in the Apache Cassandra database.

Once the ETL pipeline is finished, please open the analytical_queries.ipynb to run queries / inspect the data.

Enjoy!