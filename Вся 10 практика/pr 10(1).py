# Для заданий из практической работы №8 для своего варианта.
# Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
# И вывод результатов в файл (имя: ФИО_группа_vivod.txt).
n = int(input()) # кол-во столбцов
s = []
flag = 0
for i in range(n):
    s.append([int(x) for x in input().split()]) # числа в столбцах
for k in range(len(s) - 1):
    if sum(s[k]) == sum(s[k + 1]): # проверка по строчкам
        result = []
        for j in range(n): # диапозон от 0 до n
            y = []
            for i in range(len(s)): # список строк
                y.append(s[i][j]) # столбцы
            result.append(y) # для проверки
        for i in range(len(result) - 1):
            if sum(result[i]) == sum(result[i + 1]): # проверка по столбам
                flag = 1
            else:
                flag = 0
    else:
        flag = 0

with open('Джамалов Дмитрий Максимович_УБ-42_vvod1.txt', 'w', encoding='utf-8') as file1:
    a = file1.write(str(n))
    a = file1.write(str(s))

if flag == 1:
    with open('Джамалов Дмитрий Максимович_УБ-42_vivod1.txt', 'w', encoding='utf-8') as file2:
        a = file2.write('Квадрат является магическим')

    with open('Джамалов Дмитрий Максимович_УБ-42_vivod1.txt', 'r', encoding='utf-8') as file2:
        print(file2.read())

else:
    with open('Джамалов Дмитрий Максимович_УБ-42_vivod1.txt', 'w', encoding='utf-8') as file2:
        a = file2.write('Квадрат не является магическим')

    with open('Джамалов Дмитрий Максимович_УБ-42_vivod1.txt', 'r', encoding='utf-8') as file2:
        print(file2.read())
