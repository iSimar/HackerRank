from math import sqrt

t = input()
o = []

for x in range(t):
	a, b = [int(x) for x in raw_input().split(" ")]
	count = 0
	for i in range(a, b+1):
		if (sqrt(i)).is_integer():
			count += 1
	o += [count]

for x in o:
	print x