import math

def xor(a, b):
	bin_a = bin(a)[2:]
	bin_b = bin(b)[2:]
	n = max(len(bin_a), len(bin_b))
	o = ""
	for x in range(n):
		if(x <= len(bin_a) - 1):
			if(x <= len(bin_b) -1):
				if bin_a[len(bin_a)-1-x] is not bin_b[len(bin_b)-1-x]:
					o="1"+o
				else:
					o="0"+o
			else:
				o="1"+o
		else:
			o="1"+o
	return int(o, 2)


l = input()
r = input()
maxXOR = None

for x in range(l, r+1):
	for y in range(x, r+1):
		XOR = xor(x, y)
		# print str(x) +" - "+ str(y) + " = " + str(XOR)
		if maxXOR is not None:
			if maxXOR <= XOR:
				maxXOR = XOR
		else:
			maxXOR = XOR

print maxXOR