n = 3 #кол-во столбцов в кубе
a = []
for i in range(n):
    a.append([int(i) for i in input().split()]) #числа куба
x, y, z = sum(a[0]), sum(a[1]), sum(a[2]) #сумма чисел в строке
if x == y == z:
    s1, s2, s3, d1, d2, d3, f1, f2, f3 = a[0][0], a[0][1], a[0][-1], a[1][0], a[1][1], a[1][-1], a[-1][0], a[-1][1], a[-1][-1]
    sums, sumd, sumf = s1 + d1 + f1, s2 + d2 + f2, s3 + d3 + f3 #сумма чисел в столбце
    if sums == sumd == sumf:
        print('Куб является магическим')
    else:
        print('Куб не является магическим')
else:
    print('Куб не является магическим')
