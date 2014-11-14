def numOfPalindromeOperations(s):
	numOfOperations = 0
	for i in range(len(s)):
		ascii_1 = ord(s[i])
		ascii_2 = ord(s[len(s)-1-i])
		if ascii_1<ascii_2:
			numOfOperations += ascii_2 - ascii_1
	return numOfOperations

t = input()
output = []

for x in range(t):
	c = raw_input()
	output += [numOfPalindromeOperations(c)]

for x in output:
	print x