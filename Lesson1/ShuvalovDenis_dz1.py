import json
import requests


username = input(str("Введите имя пользователя:")) # DenisShuvalov
url = f'https://api.github.com/users/{username}/repos'

responce = requests.get(url)

if responce.ok == 1:  # проверка ответа сервера
    responce.raise_for_status()
    data = responce.json()  # проверка на json
    with open('user_repos.json', 'w', encoding='utf-8') as file:  # сохраняем в файл
        json.dump(data, file, indent=2, ensure_ascii=False)
print(responce.status_code)
