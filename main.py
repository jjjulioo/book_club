import pandas as pd 
import mysql.connector
from database import table_exists, create_table, insert_books

# Read CSV file into a DataFrame
df = pd.read_csv('books.csv')  # Ensure 'books.csv' is the path to your CSV file

if table_exists() == False:
    create_table()
else: 
    print(df)
    print(df.iterrows)
    insert_books(df.iterrows())
