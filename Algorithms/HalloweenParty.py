def maxNumOfPieces(k):
	maxNum = 0
	for x in range(1, k+1, 1):
		a = k - x
		if a*x > maxNum:
			maxNum = a*x
	return maxNum

t = input()
o = []

for x in range(t):
	c = input()
	o += [maxNumOfPieces(c)]

for x in o:
	print x