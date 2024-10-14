import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(host='localhost', user='root', password='root', database='book_club')
cursor = connection.cursor()

def table_exists():
    # Check if the table exists
    table_name = 'books'
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.tables 
        WHERE table_name = '{table_name}' 
        AND table_schema = '{connection.database}'
    """)

    if cursor.fetchone()[0] == 0:
        return False
    else:
        print(f"Table '{table_name}' already exists.") 
        return True

def create_table(): 

    create_table_query = """
    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        publication_date YEAR
    )
    """
    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created.")

    return None

# Check if the table exists
table_name = 'books'
cursor.execute(f"""
    SELECT COUNT(*)
    FROM information_schema.tables 
    WHERE table_name = '{table_name}' 
      AND table_schema = '{connection.database}'
""")

if cursor.fetchone()[0] == 0:
    create_table_query = """
    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        publication_date YEAR
    )
    """
    cursor.execute(create_table_query)
    print(f"Table '{table_name}' created.")

else:
    print(f"Table '{table_name}' already exists.")


def insert_books(df):
    # Insert DataFrame into MySQL
    for _, row in df:
        insert_query = """
        INSERT INTO books (title, author, publication_date) VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (row['title'], row['author'], row['publication_date']))

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Data inserted successfully!")