import requests
from database import create_teble_users, insert_fake_users, create_table_posts, insert_posts, create_table_albums, \
    insert_albums, create_table_photos, insert_photos, create_table_todos, insert_todos, create_table_comments, \
    insert_comments, create_table_weather, insert_weather
import json
from pprint import pprint
import sqlite3
from datetime import datetime


def get_json(link):
    data = requests.get(link).json()
    return data


def get_data():
    create_teble_users()
    data = get_json('https://dummyjson.com/users')
    users = data['users']
    for user in users:
        name = user['firstName']
        email = user['email']
        phone = user['phone']
        print(f'Name: {name}, email: {email}, phone: {phone}')

        insert_fake_users(name=name,
                          email=email,
                          phone=phone)


get_data()

# create_table_posts()
# posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
# pprint(posts)
#
# posts_list = []
# for post in posts:
#     userId = post['userId']
#     id = post['id']
#     title = post['title']
#     body = post['body']
#     posts_list.append({
#         'userId': userId,
#         'id': id,
#         'title': title,
#         'body': body
#     })
#     insert_posts(id=id,
#                  userId=userId,
#                  title=title,
#                  body=body)
#
# create_table_comments()
# comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
# pprint(comments)
#
#
# comments_list = []
# for comment in comments:
#     postId = comment['postId']
#     id = comment['id']
#     name = comment['name']
#     email = comment['email']
#     body = comment['body']
#     comments_list.append({
#         'postId': postId,
#         'id': id,
#         'name': name,
#         'email': email,
#         'body': body
#     })
#     insert_comments(id=id,
#                     postId=postId,
#                     name=name,
#                     email=email,
#                     body=body)
#
#
# create_table_albums()
# albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()
# pprint(albums)
#
#
# albums_list = []
# for album in albums:
#     userId = album['userId']
#     id = album['id']
#     title = album['title']
#     albums_list.append({
#         'userId': userId,
#         'id': id,
#         'title': title
#     })
#     insert_albums(id=id,
#                   userId=userId,
#                   title=title)
#
#
# create_table_photos()
# photos = requests.get('https://jsonplaceholder.typicode.com/photos').json()
# pprint(photos)
#
#
# photos_list = []
# for photo in photos:
#     albumId = photo['albumId']
#     id = photo['id']
#     title = photo['title']
#     url = photo['url']
#     photos_list.append({
#         'albumId': albumId,
#         'id': id,
#         'title': title,
#         'url': url,
#     })
#     insert_photos(id=id,
#                   albumId=albumId,
#                   title=title,
#                   url=url,)
#
#
# create_table_todos()
# todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
# pprint(todos)
#
# todos_list = []
# for tod in todos:
#     userId = tod['userId']
#     id = tod['id']
#     title = tod['title']
#     completed = tod['completed']
#     todos_list.append({
#         'userId': userId,
#         'id': id,
#         'title': title,
#         'completed': completed
#     })
#     insert_todos(id=id,
#                  userId=userId,
#                  title=title,
#                  completed=completed)
#
#

create_table_weather()
parameters = {
    'appid': '137d62f3c460fac41edca5930e84af7c',
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city = input('Введите название города: ')
    if city == 'stop':
        break
    parameters['q'] = city
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        timezone = data['timezone']
        # Как нам перевести время в человеческий вид
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'] + timezone).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset'] + timezone).strftime('%H:%M:%S')
        print(f'''В городе {city} сейчас {description}
Температура: {temp}
Скорость ветра: {wind_speed}
Рассвет: {sunrise}
Закат: {sunset}''')
        insert_weather(
                       city=city,
                       temp=temp,
                       wind=wind_speed,
                       description=description,
                       sunrise=sunrise,
                       sunset=sunset)
    except Exception as e:
        print(e)
        print('Не верный город. Попробуйте снова')
