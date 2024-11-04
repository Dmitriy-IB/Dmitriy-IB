n = int(input()) #кол-во столбцов
li = []
flag = 0
for i in range(n):
    li.append([int(x) for x in input().split()]) #числа в столбцах
for k in range(len(li) - 1):
    if sum(li[k]) == sum(li[k + 1]): #проверка по строчкам
        res = []
        for j in range(n): #диапозон от 0 до n
            pr = []
            for i in range(len(li)): #список строк
                pr.append(li[i][j]) #столбцы
            res.append(pr) #для проверки
        for i in range(len(res) - 1):
            if sum(res[i]) == sum(res[i + 1]): #проверка по столбам
                flag = 1
            else:
                flag = 0
    else:
        flag = 0
if flag == 1:
    print('Квадрат  магический')
else:
    print('Квадрат не магический')