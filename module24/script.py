import sqlite3



conn=sqlite3.connect('pyadvanced24.db')
cursors=conn.cursor()

cursors.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age NUMERIC not null,
        email TEXT not null
    );
''')


cursors.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id int PRIMARY KEY,
        product_name TEXT NOT NULL,
        price NUMERIC not null
    
    );
''')

cursors.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        id int PRIMARY KEY,
        date_time TEXT,
        place TEXT NOT NULL,
        user_ID INTEGER,
        product_ID INTEGER,
        FOREIGN KEY (user_ID) REFERENCES users(id),
        FOREIGN KEY (product_ID) REFERENCES products(id)

    );
''')
# cursors.execute("INSERT INTO products(product_name, price) VALUES ('Iphone 18', 1500);")
# cursors.execute("INSERT INTO orders(date_time, place ,user_ID,product_ID ) VALUES ('17-10-2026 12:39','XK', 2, 1);")
# cursors.execute("UPDATE products SET ID=1")

conn.commit()

# cursors.execute('''
#     SELECT p.product_name, u.name, o.*
#     FROM orders o INNER JOIN products p
#     ON o.product_ID==p.id INNER JOIN users u
#     ON u.id=o.user_ID;
# ''')
# records_from_db=cursors.fetchall()
# for row in records_from_db:
#     print(row)
