def minOfDeletions(string_):
	minNum = 0
	for i in range(len(string_)):
		if i is not len(string_) - 1:
			if string_[i] is string_[i+1]:
				minNum = minNum + 1
	return minNum

t = input()
output = []

for i in range(t):
	c = raw_input()
	output += [minOfDeletions(c)]

for x in output:
	print x