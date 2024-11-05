def ost(a, b):
    if a % b == 0:
        return 1
    if a < b:
        return 0
    return a % b
a = int(input())
b = int(input())
print(ost(a, b))
