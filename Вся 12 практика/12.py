# Задание: даны самые популярные репозитории на github, по последней цифре зачетки получить JSON для вашего варианта.
# Программа с графическим интерфейсом вводим в поле имя репозитория и по нажатию кнопки получаем результат.
# Необходимо получить в новый файл следующую информацию:'company' 'created_at' 'email' 'id' 'name' 'url'
# Вcе прикрепить одним архивом.
from tkinter import *
import json
import requests

def polychit():
    username = entry.get() # вводим имя репрезитория
    url = f"https://api.github.com/users/{username}" # ссылка для получения информации
    req = requests.get(url) # запрос информации из ссылки
    with open('dannie.json', 'w') as soxranenie:
        json.dump(req.json(), soxranenie) # записывает файл в json формате
    with open('dannie.json', 'r') as soxranenie:
        zagruzka = json.load(soxranenie) # считываем json файл
        klyuchi = {
            'company': (zagruzka['company']),
            'created_at': (zagruzka['created_at']),
            'email': (zagruzka['email']),
            'id': (zagruzka['id']),
            'name': (zagruzka['name']),
            'url': (zagruzka['url'])
        } # необходимая часть данных (ключей), полученных из API GitHub
        with open('dannie.json', 'w', ) as vivod:
            json.dump(info, vivod, indent=4) # перезапись json файла только с нужными ключами с 4-мя пробелами

root = Tk()
root.title('Джамалов Дмитрий Максимович')
root.geometry('400x300+750+375')
root.resizable(False, False)
entry = Entry(root) # поле для ввода репрезитория
entry.pack()
but = Button(root, text='Вывести информацию', command=polychit) #
but.pack()

root.mainloop()