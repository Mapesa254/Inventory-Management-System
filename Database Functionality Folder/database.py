# database.py

import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        #Initialize the database connection.
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        #Create a database connection to the SQLite database.
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to SQLite database: {db_file}")
        except Error as e:
            print(f"Error: {e}")
        return conn

    def create_table(self, create_table_sql):
        #Create a table using the provided SQL statement.
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            print("Table created successfully.")
        except Error as e:
            print(f"Error: {e}")

    def execute_query(self, query, data=None):
        #Execute a general SQL query.
        try:
            cursor = self.conn.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            self.conn.commit()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error: {e}")

    def fetch_data(self, query):
        #Fetch data from the database.
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return []

    def close_connection(self):
        #Close the database connection.
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
