k = 0
x = input()
k += x.count(':')
x = x.replace(':', '%')
print(k, x)
