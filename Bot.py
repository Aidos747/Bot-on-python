from datetime import datetime
import random
import json
import requests

jokes = ['Колобок повесился', 'Стэтхем гладит рубашки взглядом', 'Сидим не рыпаемся']
quotes = [
    'Я не злой. Просто если я улыбаюсь — у людей начинаются подозрения.',
    'Я не дерусь без причины. Причину я узнаю потом.',
    'Когда я захожу в бар, Wi-Fi сам отключается от страха.'
]

API_Key = "https://api.openweathermap.org/data/2.5/weather?q=Shymkent&appid=136d68508a9d82d44de7a6f9bac018b2&units=metric"

def get_weather():
    url = API_Key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        print(f'Температура: {main["temp"]}°C')
        print(f'Давление: {main["pressure"]} hPa')
        print(f'Влажность: {main["humidity"]}%')
        print(f'Скорость ветра: {wind["speed"]} м/с')
        print(f'Описание: {weather["description"]}')
    else:
        print('Ошибка получения данных о погоде')

data = {}
get_name = input('Введите ваше имя - ')
data['name'] = get_name
with open("database.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Здравствуйте {get_name}')

menu = """
====================================
    Выберите действие, введя цифру:
    1. Шутка дня
    2. Текущее время
    3. Цитата
    4. Погода
    5. Выход
====================================
"""

while True:
    print(menu)
    command = input("Введите номер команды (1-5): ")

    if command == '1':
        print(f"Шутка: {random.choice(jokes)}")
    elif command == '2':
        print(f"Сейчас: {datetime.now().strftime('%H:%M:%S')}")
    elif command == '3':
        print(f"Цитата: {random.choice(quotes)}")
    elif command == '4':
        print("Прогноз погоды: ")
        get_weather()
    elif command == '5':
        print("До встречи! Хорошего дня!")
        break
    else:
        print("Ошибка: Введите число от 1 до 5.")