# Import Python packages 
import pandas as pd
import re
import os
import glob
import numpy as np
import json
import csv

def create_filepath_list():
    '''
    Iterates through /data and returns a list of the files' absolute path.
    '''
    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    # Used this method to avoid appending jupyter checkpoint to the list
    filepath_list = [os.path.join(filepath, file) for file in os.listdir(filepath) if file.endswith('.csv')]
    
    return filepath_list

def preprocess_csv_data(filepath_list):
    '''
    Preprocesses CSV files (/data folder) in one CSV file.
    This will be used later to be loaded into an Apache Cassandra Keyspace 
    '''
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 

    # for every filepath in the file path list 
    for f in filepath_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)

     # extracting each data row one by one and append it        
            for line in csvreader:
                full_data_rows_list.append(line) 

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    NEWFILE = 'event_datafile_new.csv'
    with open(NEWFILE, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
            
    print(f"{NEWFILE} is outputted.")
    
def main():
    filepath_list = create_filepath_list()
    preprocess_csv_data(filepath_list)
    print("Preprocessing is finished.\n") 
    
if __name__ == "__main__":
    main()