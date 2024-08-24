import tkinter as tk
from tkinter import messagebox
from inventory_db import InventoryDB

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        # Create InventoryDB instance
        self.inventory_db = InventoryDB("inventory_management.db")
        
        # Add Product Button
        self.add_product_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_product_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Update Stock Button
        self.update_stock_button = tk.Button(root, text="Update Stock", command=self.update_stock)
        self.update_stock_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Display Inventory Button
        self.display_inventory_button = tk.Button(root, text="Display Inventory", command=self.display_inventory)
        self.display_inventory_button.grid(row=0, column=2, padx=10, pady=10)
        
    def add_product(self):
        # You can add more fields for category, price, etc.
        product_name = tk.simpledialog.askstring("Input", "Enter product name:")
        category = tk.simpledialog.askstring("Input", "Enter product category:")
        price = tk.simpledialog.askfloat("Input", "Enter product price:")
        quantity = tk.simpledialog.askinteger("Input", "Enter product quantity:")
        
        if product_name and category and price and quantity is not None:
            self.inventory_db.add_product(product_name, category, price, quantity)
            messagebox.showinfo("Success", "Product added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all the fields.")
        
    def update_stock(self):
        product_id = tk.simpledialog.askinteger("Input", "Enter product ID:")
        new_quantity = tk.simpledialog.askinteger("Input", "Enter new stock quantity:")
        
        if product_id and new_quantity is not None:
            self.inventory_db.update_stock(product_id, new_quantity)
            messagebox.showinfo("Success", "Stock updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all the fields.")
        
    def display_inventory(self):
        inventory = self.inventory_db.get_inventory()
        inventory_str = "\n".join([f"ID: {prod[0]}, Name: {prod[1]}, Category: {prod[2]}, Price: {prod[3]}, Stock: {prod[4]}" for prod in inventory])
        messagebox.showinfo("Inventory", inventory_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
