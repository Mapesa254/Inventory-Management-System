# supplier.py
# Class to manage supplier information and performance.

class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        """
        Initialize a new Supplier instance.
        
        :param supplier_id: Unique identifier for the supplier
        :param name: Name of the supplier
        :param contact_info: Contact information for the supplier
        """
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info
        self.performance = []

    def add_performance_record(self, record):
        """
        Add a performance record for the supplier.
        
        :param record: Performance record to add (e.g., delivery time, accuracy)
        """
        self.performance.append(record)

    def get_supplier_info(self):
        """
        Retrieve supplier information and performance metrics.
        
        :return: Dictionary containing supplier details and performance metrics
        """
        return {
            'supplier_id': self.supplier_id,
            'name': self.name,
            'contact_info': self.contact_info,
            'performance': self.performance
        }
