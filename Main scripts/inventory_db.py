# inventory_db.py
# Class to handle database operations using SQLite.

import sqlite3
from sqlite3 import Error

class InventoryDB:
    def __init__(self, db_file):
        """
        Initialize a connection to the SQLite database.
        
        :param db_file: Path to the SQLite database file
        """
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """
        Create a database connection to the SQLite database.
        
        :param db_file: Path to the SQLite database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error connecting to SQLite DB: {e}")
        return conn

    def create_table(self, create_table_sql):
        """
        Create a table in the database.
        
        :param create_table_sql: SQL statement for creating the table
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            print("Table created successfully")
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_product(self, product):
        """
        Insert a new product into the products table.
        
        :param product: Product instance to insert
        """
        sql = ''' INSERT INTO products(name, category, price, stock)
                  VALUES(?, ?, ?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (product.name, product.category, product.price, product.stock))
        self.conn.commit()

    def insert_order(self, order):
        """
        Insert a new order into the orders table.
        
        :param order: Order instance to insert
        """
        sql = ''' INSERT INTO orders(order_id, product_name, quantity, order_date, status)
                  VALUES(?, ?, ?, ?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (order.order_id, order.product.name, order.quantity, order.order_date, order.status))
        self.conn.commit()

    def insert_supplier(self, supplier):
        """
        Insert a new supplier into the suppliers table.
        
        :param supplier: Supplier instance to insert
        """
        sql = ''' INSERT INTO suppliers(supplier_id, name, contact_info)
                  VALUES(?, ?, ?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (supplier.supplier_id, supplier.name, supplier.contact_info))
        self.conn.commit()

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
