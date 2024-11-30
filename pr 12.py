import requests
import json
user_data = requests.get('https://api.github.com/users/vgstation-coders') # делаем запрос
with open('data.json', 'w') as outfile: # преобразуем в json, создаём переменную outfile и открываем файл в режиме записи
    json.dump(user_data.json(), outfile) # делаем себе копию
with open('data.json', 'r') as file: # открываем файл в режиме чтения
    data = json.load(file) # загружаем file в епременную для дальнейших опрераций
    print(('company:', data.get('company')), ('created_at:', data.get('created_at')), ('email:', data.get('email')), ('id:', data.get('id')), ('name:', data.get('name')), ('url:', data.get('url')), sep = '\n')

