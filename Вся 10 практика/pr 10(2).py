# 2 Дана прямоугольная матрица A[N, N]. Переставить первый и последний столбцы местами и вывести на экран.
n = 3 # кол-во столбцов и строк в прямоугольнике
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a_copy = a.copy()
s = a[0]
a[0] = a[-1]
a[-1] = s

with open('Джамалов Дмитрий Максимович_УБ-42_vvod2.txt', 'w', encoding='utf-8') as file1:
    b = file1.write(str(n))
    b = file1.write(str(a_copy))

with open('Джамалов Дмитрий Максимович_УБ-42_vivod2.txt', 'w', encoding='utf-8') as file2:
    c = file2.write(str(a))

with open('Джамалов Дмитрий Максимович_УБ-42_vivod2.txt', 'r', encoding='utf-8') as file2:
    print(file2.read())
