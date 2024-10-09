n = int(input())
x = [int(input()) for i in range(n)]
plus = [y for y in x if y > 0]
minus = [z for z in x if z < 0]
print(plus, minus)