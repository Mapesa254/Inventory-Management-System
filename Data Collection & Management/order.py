# order.py
# Class to manage customer orders.

class Order:
    def __init__(self, order_id, product, quantity, order_date):
        """
        Initialize a new Order instance.
        
        :param order_id: Unique identifier for the order
        :param product: Product instance associated with the order
        :param quantity: Quantity of the product ordered
        :param order_date: Date when the order was placed
        """
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.order_date = order_date
        self.status = "Pending"  # Default status for new orders

    def update_status(self, new_status):
        """
        Update the status of the order.
        
        :param new_status: New status to set for the order (e.g., 'Shipped', 'Completed')
        """
        self.status = new_status

    def get_order_details(self):
        """
        Retrieve details about the order.
        
        :return: Dictionary containing order details
        """
        return {
            'order_id': self.order_id,
            'product': self.product.get_info(),
            'quantity': self.quantity,
            'order_date': self.order_date,
            'status': self.status
        }
