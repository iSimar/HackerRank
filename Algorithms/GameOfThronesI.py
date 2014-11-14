def canBePlaidrome(s):
 	alphabets = {}
 	for x in s:
 		if x not in alphabets.keys():
 			alphabets[x] = 1
 		else:
 			alphabets[x] += 1
 	n = 0
 	for key, value in alphabets.items():
 		if value % 2 != 0:
 			n += 1
 		if n > 1:
 			return "NO"
 	return "YES"

t = raw_input()
print canBePlaidrome(t)