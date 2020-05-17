#!/bin/bash

echo "Running ETL pipeline..."
echo "Preprocessing event_data"
python3 preprocessing.py
echo "Resetting tables."
python3 create_tables.py
echo "ETL pipeline is finished. Please open analytical_queries.ipynb to access the database."

