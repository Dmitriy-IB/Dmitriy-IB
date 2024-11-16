n = int(input())  # кол-во столбцов
s = []
flag = 0
for i in range(n):
    s.append([int(x) for x in input().split()])

file1 = open('Джамалов Дмитрий Максимович_УБ-42_vvod .txt', 'w')
a = file1.write(str('3\n 5 12 7\n 10 8 6\n 9 4 11'))
file1.close()

file1 = open('Джамалов Дмитрий Максимович_УБ-42_vvod .txt', 'r')
b = file1.read()
file1.close()

file2 = open('Джамалов Дмитрий Максимович_УБ-42_vivod .txt', 'w')
c = file2.write(str(b))
file2.close()

file2 = open('Джамалов Дмитрий Максимович_УБ-42_vivod .txt', 'r')
print(*file2)
file2.close()