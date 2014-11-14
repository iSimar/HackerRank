n = input()
s = raw_input()
o = [n]

sticks = s.split(" ")

for i in range(len(sticks)):
	sticks[i] = int(sticks[i])

while len(sticks) > 1:
	sticks.sort()
	min_length = sticks[0]
	for i in range(len(sticks)):
		sticks[i] -= min_length
	sticks = [x for x in sticks if x != 0]
	o += [len(sticks)]

for x in o:
	print x