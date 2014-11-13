# 0 -> 1
# 1 -> 2
# 2 -> 3 
# 3 -> 6
# 4 -> 7 
# 5 -> 14
# 6 -> 15

def getHeight(cycles):
	if(cycles==0):
		return 1
	if cycles % 2 == 0:
		return getHeight(cycles-1)+1
	else:
		return 2*getHeight(cycles-1)

t = input()
output = []
for x in range(t):
	c = input()
	output += [getHeight(c)]

for x in output:
	print x