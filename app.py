import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Basic app configuration
app.config['SECRET_KEY'] = 'your_super_secret_key'  # Needed for flash messages
# Set the database URI to use a local SQLite database named 'inventory.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

# Initialize the database extension
db = SQLAlchemy(app)

# Define the Product model (Represents a table in the database)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

# Home route - Displays the admin menu
@app.route('/')
def index():
    return render_template('index.html')

# Products route - Retrieves and displays all products
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

# Add Product route - Handles both displaying the form and processing the form submission
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        
        # Create a new Product object and save to the database
        new_product = Product(name=name, description=description, category=category, price=price, stock=stock)
        db.session.add(new_product)
        db.session.commit()
        
        flash('Product added successfully!')
        return redirect(url_for('products'))
    
    return render_template('add_product.html')

# Update Product route - Edits an existing product
@app.route('/update_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    # Fetch the product by ID or return a 404 error if not found
    product = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        # Update product fields with form data
        product.name = request.form['name']
        product.description = request.form['description']
        product.category = request.form['category']
        product.price = float(request.form['price'])
        product.stock = int(request.form['stock'])
        
        db.session.commit()
        flash('Product updated successfully!')
        return redirect(url_for('products'))
        
    return render_template('update_product.html', product=product)

# Delete Product route - Removes a product from the database
@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    
    flash('Product deleted successfully!')
    return redirect(url_for('products'))

# Ensure tables are created before handling requests
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
