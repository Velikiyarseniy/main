import requests
import json
from pprint import pprint


posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
pprint(posts)


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

with open('posts.json', mode='w', encoding='UTF-8') as file:
    json.dump(posts_list, file, ensure_ascii=False, indent=4)


comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
pprint(comments)


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

    with open('comments.json', mode='w', encoding='UTF-8') as file:
        json.dump(comments_list, file, ensure_ascii=False, indent=4)



albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
pprint(albums)


albums_list = []
for album in albums:
    userId = album['userId']
    # id = albums['id']
    title = album['title']
    albums_list.append({
        'userId': userId,
        # 'id': id,
        'title': title
    })


with open('albums.json', mode='w', encoding='UTF-8') as file:
    json.dump('albums_list', file, ensure_ascii=False, indent=4)


photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
pprint(photos)


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

with open('photos.json', mode='w', encoding='UTF-8') as file:
    json.dump('photos_list', file, ensure_ascii=False, indent=4)


todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
pprint(todos)


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

with open('todos.json', mode='w', encoding='UTF-8') as file:
    json.dump('todos_list', file, ensure_ascii=False, indent=4)