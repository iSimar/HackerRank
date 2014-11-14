def gemElements(s):
	a = {}
	for x in s:
		if x not in a.keys():
			a[x] = 1
		else:
			a[x] += 1
	o = []
	for k, v in a.items():
		if v is 1:
			o += [k]
	return o

def intersection(a, b):
	o = []
	a = list(set(a))
	for x in a:
		if x in b:
			o += [x]
	return o

t = input()
common = None

for x in range(t):
	c = raw_input()
	if common is None:
		common = gemElements(c)
	else:
		common = intersection(common, gemElements(c))
	print common

print len(common)
