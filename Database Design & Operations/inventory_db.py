# inventory_db.py

from database import Database

class InventoryDB(Database):
    def __init__(self, db_file):
        #Initialize the InventoryDB and create tables.
        super().__init__(db_file)
        self.create_tables()

    def create_tables(self):
        #Create necessary tables for inventory management.
        products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL NOT NULL,
            stock_level INTEGER NOT NULL
        );
        """

        orders_table = """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products (id)
        );
        """

        suppliers_table = """
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT,
            reliability INTEGER NOT NULL DEFAULT 5
        );
        """

        self.create_table(products_table)
        self.create_table(orders_table)
        self.create_table(suppliers_table)

    def add_product(self, name, category, price, stock_level):
        #Add a new product to the products table.
        query = """
        INSERT INTO products (name, category, price, stock_level)
        VALUES (?, ?, ?, ?);
        """
        self.execute_query(query, (name, category, price, stock_level))

    def update_product_stock(self, product_id, new_stock):
        #Update the stock level of a product.
        query = """
        UPDATE products
        SET stock_level = ?
        WHERE id = ?;
        """
        self.execute_query(query, (new_stock, product_id))

    def add_order(self, product_id, quantity, order_date):
        #Add a new order to the orders table.
        query = """
        INSERT INTO orders (product_id, quantity, order_date)
        VALUES (?, ?, ?);
        """
        self.execute_query(query, (product_id, quantity, order_date))

    def add_supplier(self, name, contact, reliability=5):
        #Add a new supplier to the suppliers table.
        query = """
        INSERT INTO suppliers (name, contact, reliability)
        VALUES (?, ?, ?);
        """
        self.execute_query(query, (name, contact, reliability))

    def fetch_products(self):
        #Fetch all products from the products table.
        query = "SELECT * FROM products;"
        return self.fetch_data(query)

    def fetch_orders(self):
        #Fetch all orders from the orders table.
        query = "SELECT * FROM orders;"
        return self.fetch_data(query)

    def fetch_suppliers(self):
        #Fetch all suppliers from the suppliers table.
        query = "SELECT * FROM suppliers;"
        return self.fetch_data(query)
