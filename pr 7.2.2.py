def pl(a):
	a1 = a[0] * a[1]
	a2 = a[2] * a[3]
	a3 = a[4] * a[5]
	return a1, a2, a3
a = input()
a = a.split()
a = [int(x) for x in a]
print(pl(a))