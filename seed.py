from app import db, Product


def seed_database():
    db.create_all()

    if Product.query.first():
        print('Database already contains products. Seed skipped.')
        return

    dummy_products = [
        {
            'name': 'Wireless Ergonomic Mouse',
            'description': 'Bluetooth ergonomic mouse with programmable buttons.',
            'category': 'Electronics',
            'price': 34.99,
            'stock': 135,
        },
        {
            'name': 'Executive Hardcover Notebook',
            'description': 'A5 ruled notebook with leather-like cover, 200 pages.',
            'category': 'Stationery',
            'price': 12.99,
            'stock': 220,
        },
        {
            'name': 'Adjustable LED Desk Lamp',
            'description': 'Energy-efficient desk lamp with touch controls and USB charging.',
            'category': 'Office Supplies',
            'price': 49.95,
            'stock': 95,
        },
        {
            'name': 'Noise-Cancelling Headphones',
            'description': 'Over-ear headphones ideal for conference calls and focus work.',
            'category': 'Audio',
            'price': 89.90,
            'stock': 45,
        },
        {
            'name': 'Travel Coffee Mug',
            'description': 'Insulated stainless steel mug with leak-resistant lid.',
            'category': 'Kitchenware',
            'price': 18.50,
            'stock': 180,
        },
        {
            'name': 'Desk Filing Cabinet',
            'description': 'Compact 2-drawer steel filing cabinet with lock.',
            'category': 'Office Furniture',
            'price': 129.99,
            'stock': 30,
        },
        {
            'name': 'Inkjet Printer Paper Pack',
            'description': 'Ream of 500 sheets of premium multipurpose printer paper.',
            'category': 'Stationery',
            'price': 24.75,
            'stock': 310,
        },
        {
            'name': 'USB-C Charging Cable',
            'description': 'Durable 6-foot USB-C cable for laptops and mobile devices.',
            'category': 'Electronics Accessories',
            'price': 11.99,
            'stock': 260,
        },
        {
            'name': 'Wireless Keyboard',
            'description': 'Slim wireless keyboard with quiet keys and long battery life.',
            'category': 'Electronics',
            'price': 39.95,
            'stock': 90,
        },
        {
            'name': 'Office Chair Mat',
            'description': 'Heavy-duty chair mat for carpeted floors.',
            'category': 'Furniture Accessories',
            'price': 59.99,
            'stock': 75,
        },
        {
            'name': 'Multi-Function Shredder',
            'description': 'Cross-cut shredder for paper, credit cards and CDs.',
            'category': 'Office Equipment',
            'price': 129.00,
            'stock': 25,
        },
        {
            'name': 'Desktop Whiteboard',
            'description': 'Small magnetic whiteboard for notes and reminders.',
            'category': 'Office Supplies',
            'price': 22.49,
            'stock': 140,
        },
        {
            'name': 'Wireless Presentation Remote',
            'description': 'Presenter remote with laser pointer and slide navigation.',
            'category': 'Electronics Accessories',
            'price': 27.99,
            'stock': 85,
        },
        {
            'name': 'Sanitizing Wipes Refill',
            'description': 'Pack of disinfecting wipes for office surfaces.',
            'category': 'Cleaning Supplies',
            'price': 15.60,
            'stock': 400,
        },
        {
            'name': 'First Aid Kit',
            'description': 'Compact office first aid kit with bandages and antiseptic wipes.',
            'category': 'Safety',
            'price': 32.50,
            'stock': 55,
        },
    ]

    for item in dummy_products:
        product = Product(
            name=item['name'],
            description=item['description'],
            category=item['category'],
            price=item['price'],
            stock=item['stock'],
        )
        db.session.add(product)

    db.session.commit()
    print(f'Seeded {len(dummy_products)} products into inventory.db.')


from app import app

if __name__ == '__main__':
    with app.app_context():
        seed_database()
