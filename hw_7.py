import sqlite3

def create_table(db_name,create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE NOT NULL DEFAULT 0.0 CHECK(price >= 0 AND price < 1000000000),
    quantity INTEGER NOT NULL DEFAULT 0)

'''

def insert_products(db_name,product):
    sql = '''INSERT INTO products (product_title,price,quantity)
    VALUES (?,?,?)
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,product)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(db_name, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(db_name, pricee):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, pricee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(db_name, quatityy):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, quatityy)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_name):
    sql = '''SELECT rowid, * FROM products ORDER BY rowid '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_price_quantity(db_name, price_limit, quantity_limit):
    sql = '''SELECT id, product_title, price, quantity FROM products WHERE price < ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Error: {e}")

def search_products_by_name(db_name, search_term):
    sql = '''SELECT id, product_title, price, quantity 
             FROM products 
             WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (f"%{search_term}%",))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Error: {e}")

db_name = '''hw.db'''
create_table(db_name, sql_to_create_products_table)

insert_products(db_name,('яблоко',10.5,1))
insert_products(db_name,('мыло',20.2,2))
insert_products (db_name,('жидкое мыло',30.5,3))
insert_products(db_name,("банан", 15.0, 40))
insert_products(db_name, ("сахар", 50.0, 25))
insert_products(db_name, ("мука", 40.0, 15))
insert_products (db_name,("соль", 5.0, 100))
insert_products (db_name,("перец", 12.5, 80))
insert_products (db_name,("шампунь", 120.0, 10))
insert_products (db_name,("гель для душа", 150.0, 5))
insert_products (db_name,("рис", 30.0, 50))
insert_products (db_name,("гречка", 70.0, 35))
insert_products (db_name,("макароны", 45.0, 60))
insert_products (db_name,("масло", 110.0, 25))
insert_products (db_name,("кетчуп", 90.0, 40))

delete_product(db_name,15)

update_price(db_name,(12.5,2))
update_quantity(db_name,(5,1))

select_all_products(db_name)
select_price_quantity(db_name,20,5)
search_products_by_name(db_name, "мыло")









