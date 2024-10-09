def tr(a):
	return (3**(0.5) * a**2)/4
def shest(a):
	return 6 * tr(a)
a = int(input())
s = shest(a)
print(s)