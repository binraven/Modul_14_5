import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    
    )
    """)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL  
    )
    ''')

    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    connection.commit()
    return cursor.fetchall()

def is_included(username):
    check = cursor.execute(f"SELECT username FROM Users WHERE username = ?", (username,))
    if check.fetchone() is None:
        return False
    else:
        return True

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ? , ? , ?)",
                   (username, email, age, 1000))
    connection.commit()


# initiate_db()
# for i in range(1,5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f"Продукт{i}", f"Описание{i}", i * 100))


