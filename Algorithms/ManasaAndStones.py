# binary recursion tree of height n
# Example with n = 3, a = 1, b = 2
#       0
#     /   \
#    1     2
#   / \   / \
#  2   3 3   4


#---------- First Try - (Problem: SLOW) ---------

# def stones(n, v, a, b):
# 	if n is 1:
# 		return [v]
# 	else:
# 		o = []
# 		o += stones(n-1, v+a, a, b)
# 		o += stones(n-1, v+b, a, b)
# 		return list(set(o))


# t = input()
# o = []

# for x in range(t):
# 	n = input()
# 	a = input()
# 	b = input()
# 	lastStones = stones(n, 0, a, b)
# 	lastStones.sort()
# 	o += [" ".join([str(x) for x in lastStones])]

# for x in o:
# 	print x

#------ Second Try --------------
from math import pow

t = input()
o = []

for x in range(t):
	n = input()
	a = input()
	b = input()
	lastStones = []
	for x in range(0, n):
		y = n - x - 1
		p = a*y + b*x
		if p not in lastStones:
			lastStones += [int(p)]
	lastStones.sort()
	o += [" ".join([str(x) for x in lastStones])]

for x in o:
	print x
