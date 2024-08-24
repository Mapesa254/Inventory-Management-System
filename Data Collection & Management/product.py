# product.py
# Class to handle product-related data and operations.

class Product:
    def __init__(self, name, category, price, stock):
        """
        Initialize a new Product instance.
        
        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        :param stock: Initial stock level of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """
        Update the stock level of the product.
        
        :param quantity: Amount to add to the current stock level
        """
        self.stock += quantity

    def get_info(self):
        """
        Retrieve product information.
        
        :return: Dictionary containing product details
        """
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock
        }
