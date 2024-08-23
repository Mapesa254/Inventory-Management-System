# main.py

from inventory_db import InventoryDB

if __name__ == "__main__":
    # Initialize the InventoryDB
    inventory_db = InventoryDB("inventory_management.db")

    # Add products
    inventory_db.add_product("Product A", "Category 1", 19.99, 100)
    inventory_db.add_product("Product B", "Category 2", 29.99, 150)

    # Update product stock
    inventory_db.update_product_stock(1, 90)

    # Add orders
    inventory_db.add_order(1, 10, "2024-08-23")
    inventory_db.add_order(2, 15, "2024-08-23")

    # Add suppliers
    inventory_db.add_supplier("Supplier 1", "123-456-7890")
    inventory_db.add_supplier("Supplier 2", "098-765-4321", reliability=4)

    # Fetch and display products
    products = inventory_db.fetch_products()
    print("Products:", products)

    # Fetch and display orders
    orders = inventory_db.fetch_orders()
    print("Orders:", orders)

    # Fetch and display suppliers
    suppliers = inventory_db.fetch_suppliers()
    print("Suppliers:", suppliers)

    # Close the database connection
    inventory_db.close_connection()
