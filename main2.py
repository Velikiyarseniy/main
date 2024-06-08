import requests
import json
from pprint import pprint
import sqlite3


posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
pprint(posts)

database = sqlite3.connect('hmk json.db')
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

posts_list = []
for post in posts:
    userId = post['userId']
    id = post['id']
    title = post['title']
    body = post['body']
    posts_list.append({
        'userId': userId,
        'id': id,
        'title': title,
        'body': body
    })
    cursor.execute('''
    INSERT INTO posts(id, userId, title, body) VALUES
    (?,?,?,?)
    ''', (id, userId, title, body))
    database.commit()


with open('posts.json', mode='w', encoding='UTF-8') as file:
    json.dump(posts_list, file, ensure_ascii=False, indent=4)


comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
pprint(comments)

database = sqlite3.connect('hmk json.db')
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

comments_list = []
for comment in comments:
    postId = comment['postId']
    id = comment['id']
    name = comment['name']
    email = comment['email']
    body = comment['body']
    comments_list.append({
        'postId': postId,
        'id': id,
        'name': name,
        'email': email,
        'body': body
    })
    cursor.execute('''
    INSERT INTO comments(id, postId, name, email, body) VALUES
    (?,?,?,?,?)
    ''', (id, postId, name, email, body))
    database.commit()

with open('comments.json', mode='w', encoding='UTF-8') as file:
    json.dump(comments_list, file, ensure_ascii=False, indent=4)



albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
pprint(albums)

database = sqlite3.connect('hmk json.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    title TEXT
);
''')
database.commit()

albums_list = []
for album in albums:
    userId = album['userId']
    # id = albums['id']
    title = album['title']
    albums_list.append({
        'userId': userId,
        #'id': id,
        'title': title
    })
    cursor.execute('''
    INSERT INTO albums( userId, title) VALUES
    (?,?)
    ''', (userId, title))
    database.commit()

with open('albums.json', mode='w', encoding='UTF-8') as file:
    json.dump('albums_list', file, ensure_ascii=False, indent=4)


photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
pprint(photos)

database = sqlite3.connect('hmk json.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS photos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    albumId INTEGER,
    title TEXT,
    url TEXT,
    thumbnaiUrl
);
''')
database.commit()

photos_list = []
for photo in photos:
    albumId = photo['albumId']
    id = photo['id']
    title = photo['title']
    url = photo['url']
    thumbnailUrl = photo['thumbnailUrl']
    photos_list.append({
        'albumId': albumId,
        'id': id,
        'title': title,
        'url': url,
        'thumbnailUrl': thumbnailUrl
    })
    cursor.execute('''
    INSERT INTO photos(id, albumId, title, url, thumbnaiUrl) VALUES
    (?,?,?,?,?)
    ''', (id, albumId, title, url, thumbnailUrl))
    database.commit()

with open('photos.json', mode='w', encoding='UTF-8') as file:
    json.dump('photos_list', file, ensure_ascii=False, indent=4)


todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
pprint(todos)

database = sqlite3.connect('hmk json.db')
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


todos_list = []
for tod in todos:
    userId = tod['userId']
    id = tod['id']
    title = tod['title']
    completed = tod['completed']
    todos_list.append({
        'userId': userId,
        'id': id,
        'title': title,
        'completed': completed
    })
    cursor.execute('''
    INSERT INTO todos(userId, id, title, completed) VALUES
    (?,?,?,?)
    ''', (userId, id, title, completed))
    database.commit()

with open('todos.json', mode='w', encoding='UTF-8') as file:
    json.dump('todos_list', file, ensure_ascii=False, indent=4)

