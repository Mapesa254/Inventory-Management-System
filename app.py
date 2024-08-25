from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        new_product = Product(name=name, description=description, category=category, price=price, stock=stock)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('products'))
    return render_template('add_product.html')

@app.route('/update_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.category = request.form['category']
        product.price = float(request.form['price'])
        product.stock = int(request.form['stock'])
        db.session.commit()
        flash('Product updated successfully!')
        return redirect(url_for('products'))
    return render_template('update_product.html', product=product)

@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!')
    return redirect(url_for('products'))

if __name__ == '__main__':
    app.run(debug=True)
