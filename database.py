import sqlite3


# Funksiya mijozni tablisasi

def create_users_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
    );
    ''')
    database.commit()
    database.close()


# create_users_table()

# Karzinani ozi
def create_carts_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),
        total_price DECIMAL(12, 2 ) DEFAULT 0,
        total_products INTEGER DEFAULT 0
    );
    ''')
    database.commit()
    database.close()


# create_carts_table()

# Produktlar saqlovchi jadval
def create_cart_products_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart_products(
            cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30),
            quantity INTEGER NOT NULL,
            final_price DECIMAL(12, 2) NOT NULL,
            cart_id INTEGER REFERENCES carts(cart_id),
            
            UNIQUE(product_name, cart_id)
        );
    ''')
    database.commit()
    database.close()


# create_cart_products_table()

# Kategoriya jadvali yaratish
def create_categories_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(20) NOT NULL UNIQUE
        );
    ''')
    database.commit()
    database.close()


# create_categories_table()

# kategoriyani ismlarini qoshish
def insert_categories():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Burgers'),
    ('Breakfast'),
    ('Fries & Sides'),
    ('Sweets & Treats'),
    ('Beverages'),
    ('Chicken & Fish Sandwiches')
    ''')
    database.commit()
    database.close()


# insert_categories()


def create_products_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(30) NOT NULL UNIQUE,
        price DECIMAL(12, 2) NOT NULL,
        description VARCHAR(100),
        image TEXT,
        
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
        );
        ''')
    database.commit()
    database.close()


# create_products_table()


def insert_products_table():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image) VALUES
    (1, 'BigMac', 22000, 'McBigMac', 'media/Burgers/bigmac.jpg'),
    (1, 'Double BigMac', 27000, 'Mc Double BigMac', 'media/Burgers/doublebigmac.jpg'),
    (1, 'Double Quarter Pounder', 28000, 'Mc Double Quarter Pounder', 'media/Burgers/doublequarterpounder.jpg'),
    (1, 'Mc Double', 26000, 'McDouble', 'media/Burgers/mcdouble.jpg'),
    (1, 'Quarter Pounder with Cheese', 27000, 'McQuarter Pounder with Cheese', 'media/Burgers/quarterpounderwithcheese.jpg'),
    (1, 'Quarter Pounder with Cheese Deluxe', 26000, 'McQuarter Pounder with Cheese Deluxe', 'media/Burgers/quarterpounderwithcheesedeluxe.jpg')
    (2, 'Bacon Egg & Cheese Biscuit', 28000, 'McBacon Egg & Cheese Biscuit', 'media/Breakfast/Bacon, Egg & Cheese Biscuit.jpg')
    (2, 'Egg McMuffin®', 21000, 'McEgg McMuffin®', 'media/Breakfast/Egg McMuffin®.jpg')
    (2, 'Sausage Biscuit', 24000, 'McSausage Biscuit', 'media/Breakfast/Sausage Biscuit.jpg')
    (2, 'Sausage Biscuit with Egg', 23000, 'McSausage Biscuit with Egg', 'media/Breakfast/Sausage Biscuit with Egg.jpg')
    (2, 'Sausage McMuffin®', 27000, 'McSausage McMuffin®', 'media/Breakfast/Sausage McMuffin®.jpg')
    (2, 'Sausage McMuffin® with Egg', 29000, 'McSausage McMuffin® with Egg', 'media/Breakfast/Sausage McMuffin® with Egg.jpg')
    (3, 'Deluxe McCrispy™', 21000, 'McDeluxe McCrispy™', 'media/Chicken & Fish Sandwiches/SDeluxe McCrispy™.jpg')
    (3, 'Filet-O-Fish®', 24000, 'McFilet-O-Fish®', 'media/Chicken & Fish Sandwiches/Filet-O-Fish®.jpg')
    (3, 'McChicken®', 27000, 'McMcChicken®', 'media/Chicken & Fish Sandwiches/McChicken®.jpg')
    (3, 'McCrispy™', 29000, 'McMcCrispy™', 'media/Chicken & Fish Sandwiches/McCrispy™.jpg')
    (3, 'Spicy Deluxe McCrispy™', 22000, 'McSpicy Deluxe McCrispy™', 'media/Chicken & Fish Sandwiches/Spicy Deluxe McCrispy™.jpg')
    (3, 'Spicy McCrispy™', 25000, 'McSpicy McCrispy™', 'media/Chicken & Fish Sandwiches/Spicy McCrispy™.jpg')
    (4, 'Creamy Ranch Sauce', 25000, 'McCreamy Ranch Sauce', 'media/Fries & Sides/Creamy Ranch Sauce.jpg')
    (4, 'Honey Mustard Sauce', 27000, 'McHoney Mustard Sauce', 'media/Fries & Sides/Honey Mustard Sauce.jpg')
    (4, 'Savory Chili WcDonald’s Sauce', 29000, 'McSavory Chili WcDonald’s Sauce', 'media/Fries & Sides/Savory Chili WcDonald’s Sauce.jpg')
    (4, 'Spicy Buffalo Sauce', 22000, 'McSpicy Buffalo Sauce', 'media/Fries & Sides/Spicy Buffalo Sauce.jpg')
    (4, 'Tangy Barbeque Sauce', 24000, 'McTangy Barbeque Sauce', 'media/Fries & Sides/Tangy Barbeque Sauce.jpg')
    (4, 'World Famous Fries®', 28000, 'McWorld Famous Fries®', 'media/Fries & Sides/World Famous Fries®.jpg')
    (5, 'Chocolate Shake', 21000, 'McChocolate Shake', 'media/Sweets & Treats/Chocolate Shake.jpg')
    (5, 'McFlurry® with M&M'S® Candies', 23000, 'McMcFlurry® with M&M'S® Candies', 'media/Sweets & Treats/McFlurry® with M&M'S® Candies.jpg')
    (5, 'McFlurry® with OREO® Cookies', 25000, 'McMcFlurry® with OREO® Cookies', 'media/Sweets & Treats/McFlurry® with OREO® Cookies.jpg')
    (5, 'OREO® Shamrock McFlurry®', 27000, 'McOREO® Shamrock McFlurry®', 'media/Sweets & Treats/OREO® Shamrock McFlurry®.jpg')
    (5, 'Shamrock Shake®', 29000, 'McShamrock Shake®', 'media/Sweets & Treats/Shamrock Shake®.jpg')
    (5, 'Vanilla Cone', 22000, 'McVanilla Cone', 'media/Sweets & Treats/Vanilla Cone.jpg')
    (6, 'Coca-Cola®', 9000, 'McCoca-Cola®', 'media/Beverages/Coca-Cola®.jpg')
    (6, 'Fanta® Orange', 7000, 'McFanta® Orange', 'media/Beverages/Fanta® Orange.jpg')
    (6, 'Hot Chocolate', 5000, 'McHot Chocolate', 'media/Beverages/Hot Chocolate.jpg')
    (6, 'Hot Tea', 3000, 'McHot Tea', 'media/Beverages/Hot Tea.jpg')
    (6, 'Lemonade', 1000, 'McLemonade', 'media/Beverages/Lemonade.jpg')
    (6, 'Sprite®', 6000, 'McSprite®', 'media/Beverages/Sprite®.jpg')
    ''')
    database.commit()
    database.close()


# insert_products_table()


# Registratsiyadan otkanlar uchun baza
def first_select_user(chat_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT * from users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user


def first_register_user(chat_id, full_name):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?, ?)
    ''', (chat_id, full_name))
    database.commit()
    database.close()


def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
        UPDATE users
        SET phone = ?
        WHERE telegram_id = ?
    ''', (phone, chat_id))
    database.commit()
    database.close()


def insert_to_cart(chat_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
    (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id,))
    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')

    categories = cursor.fetchall()
    database.close()
    return categories


def get_products_by_category_id(category_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name
    FROM products WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products


def get_product_detail(product_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product


def get_user_cart_id(chat_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_id FROM carts
    WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?)
    ''', (chat_id,))
    cart_id = cursor.fetchone()[0]
    database.close()
    return cart_id


def insert_or_update_cart_product(cart_id, product, quantity, final_price):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()

    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, product_name, quantity, final_price)
        VALUES(?, ?, ?, ?)
        ''', (cart_id, product, quantity, final_price))
        database.commit()
        return True
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        where product_name =? and cart_id = ?
        ''', (quantity, final_price, product, cart_id))
        database.commit()
        return False
    finally:
        database.close()


def update_total_product_total_price(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    UPDATE carts
    SET total_products = (
    SELECT SUM(quantity) FROM cart_products
    WHERE cart_id = :cart_id
    ),
    total_price = (
    SELECT SUM(final_price) FROM cart_products
    WHERE cart_id = :cart_id
    )
    WHERE cart_id = :cart_id
    ''', {'cart_id': cart_id})
    database.commit()
    database.close()


def get_cart_products(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_name, quantity, final_price
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def get_total_products_price(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT total_products, total_price FROM carts WHERE cart_id = ?
    ''', (cart_id,))
    total_products, total_price = cursor.fetchone()  # (4, 98000)
    database.close()
    return total_products, total_price


def get_cart_product_for_delete(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_product_id, product_name
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def delete_cart_product_from_database(cart_product_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_product_id = ?
    ''', (cart_product_id,))
    database.commit()
    database.close()


def drop_cart_products_default(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    database.commit()
    database.close()


def orders_check():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_check(
    order_check_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER REFERENCES carts(cart_id),
    total_price DECIMAL(12, 2) DEFAULT 0,
    total_products INTEGER DEFAULT 0,
    time_order TEXT,
    data_order TEXT
    );
    ''')


# orders_check()

def order():
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_check_id INTEGER REFERENCES orders_check(order_check_id),
        product_name VARCHAR(100) NOT NULL,
        quantity INTEGER NOT NULL,
        final_price DECIMAL(12, 2) NOT NULL
    );
    ''')
    database.commit()
    database.close()


# order()

def save_order_check(cart_id, total_products, total_price, time_order, data_order):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders_check(cart_id, total_products, total_price, time_order, data_order)
    VALUES(?, ?, ?, ?, ?)
    ''', (cart_id, total_products, total_price, time_order, data_order))
    database.commit()
    database.close()


def get_order_check_id(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT order_check_id FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_id = cursor.fetchall()[-1][0]
    database.close()
    return order_check_id


def save_order(order_check_id, product_name, quantity, final_price):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders(order_check_id, product_name, quantity, final_price)
    VALUES(?, ?, ?, ?)
    ''', (order_check_id, product_name, quantity, final_price))
    database.commit()
    database.close()


def get_order_check(cart_id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_info = cursor.fetchall()
    database.close()
    return order_check_info


def get_detail_order(id):
    database = sqlite3.connect("McDonalds's.db")
    cursor = database.cursor()
    cursor.execute('''
        SELECT product_name, quantity, final_price FROM orders
        WHERE order_check_id = ?
    ''', (id,))
    detail_order = cursor.fetchall()
    database.close()
    return detail_order
