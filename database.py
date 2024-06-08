import sqlite3

def create_teble_users():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fake_users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        email TEXT,
        phone INTEGER
    )
    ''')
    database.commit()
    database.close()

def insert_fake_users(name, email, phone):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO fake_users(name, email, phone)
    VALUES (?, ?, ?) ON CONFLICT DO NOTHING;
    ''', (name, email, phone))
    database.commit()
    database.close()

def create_table_posts():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    title TEXT,
    body TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_posts(id, userId, title, body):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO posts(id, userId, title, body) VALUES
    (?,?,?,?) ON CONFLICT DO NOTHING;
    ''', (id, userId, title, body))
    database.commit()
    database.close()

def create_table_comments():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    postId INTEGER,
    name TEXT,
    email TEXT,
    body TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_comments(id, postId, name, email, body):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO comments(id, postId, name, email, body) VALUES
    (?,?,?,?,?) ON CONFLICT DO NOTHING;
    ''', (id, postId, name, email, body))
    database.commit()
    database.close()

def create_table_albums():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    title TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_albums(id, userId, title):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO albums(id, userId, title) VALUES
    (?,?,?) ON CONFLICT DO NOTHING;
    ''', (id, userId, title))
    database.commit()
    database.close()

def create_table_photos():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS photos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    albumId INTEGER,
    title TEXT,
    url TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_photos(id, albumId, title, url):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO photos(id, albumId, title, url) VALUES
    (?,?,?,?) ON CONFLICT DO NOTHING;
    ''', (id, albumId, title, url))
    database.commit()
    database.close()

def create_table_todos():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    title TEXT,
    completed TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_todos(id, userId, title, completed):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO todos(id, userId, title, completed) VALUES
    (?,?,?,?) ON CONFLICT DO NOTHING;
    ''', (id, userId, title, completed))
    database.commit()
    database.close()


def create_table_weather():
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather(
        city TEXT,
        temp TEXT,
        wind TEXT,
        description TEXT,
        sunrise TEXT,
        sunset TEXT
    );
    ''')
    database.commit()
    database.close()

def insert_weather(city, temp, wind, description, sunrise, sunset):
    database = sqlite3.connect('opat_dz.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO weather(city, temp, wind, description, sunrise, sunset) VALUES
    (?,?,?,?,?,?) ON CONFLICT DO NOTHING;
    ''', (city, temp, wind, description, sunrise, sunset))
    database.commit()
    database.close()