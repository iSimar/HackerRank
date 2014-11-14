#N = dollars in his pocket
#C = price of each chocolate
#M = number of wrappers (one chocolate for free)

from math import floor

def wrappersToCandy(w, m):
	if w < m:
		return 0
	else:
		return 1 + wrappersToCandy(w-m+1, m)

t = input()
o = []

for x in range(t):
	n, c, m = [int(x) for x in raw_input().split(" ")]
	w = int(floor(n/c))
	o += [w + wrappersToCandy(w, m)]

for x in o:
	print x



