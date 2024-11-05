n = int(input()) #кол-во столбцов
s = []
flag = 0
for i in range(n):
    s.append([int(x) for x in input().split()]) #числа в столбцах
for k in range(len(s) - 1):
    if sum(s[k]) == sum(s[k + 1]): #проверка по строчкам
        result = []
        for j in range(n): #диапозон от 0 до n
            y = []
            for i in range(len(s)): #список строк
                y.append(s[i][j]) #столбцы
            result.append(y) #для проверки
        for i in range(len(result) - 1):
            if sum(result[i]) == sum(result[i + 1]): #проверка по столбам
                flag = 1
            else:
                flag = 0
    else:
        flag = 0
if flag == 1:
    print('Квадрат  магический')
else:
    print('Квадрат не магический')