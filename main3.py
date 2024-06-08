import requests
from datetime import datetime
import sqlite3
# Запросы на сервис погоды и получать текущую погоду в городе

parameters = {
    'appid': '137d62f3c460fac41edca5930e84af7c',
    'units': 'metric',
    'lang': 'ru'
}
database = sqlite3.connect('hmk json.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temp TEXT,
    wind TEXT,
    description TEXT,
    sunrise TEXT,
    sunset TEXT
);
''')
database.commit()


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

        cursor.execute('''
        INSERT INTO weather(city, temp, wind, description, sunrise, sunset) VALUES 
        (?,?,?,?,?,?)
        ''', (city, temp, wind_speed, description, sunrise, sunset))
        database.commit()
        print(f'''В городе {city} сейчас {description}
Температура: {temp}
Скорость ветра: {wind_speed}
Рассвет: {sunrise}
Закат: {sunset}''')
    except Exception as e:
        print(e)
        print('Не верный город. Попробуйте снова')