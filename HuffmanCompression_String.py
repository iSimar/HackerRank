print "Enter a string you want compressed:"
m = raw_input("")
# m = "MISSISSIPPI RIVER" #For testing

#simple binary tree node class
class node:
	left = None
	val = None
	right = None
	# parent = None

	def __init__(self, l, v, r):
		self.left = l
		self.val = v
		self.right = r

def intToBits(i):
	if i == 0:
		return "0"
	if i == 1:
		return '1'
	d = float(i)/2
	t = d - int(d)
	if t == 0:
		return intToBits(int(d)) + '0'
	else:
		return intToBits(int(d)) + '1'

def make8Bit(s, n=8):
	if len(s) < n:
		return make8Bit('0'+s)
	return s

def stringToBits(s):
	bits = ""
	for c in s:
		bits += make8Bit(intToBits(ord(c)))
	return bits

def buildHuffmanCompressionTree(leafs):
	if len(leafs)==1:
		return leafs[0]

	min1 = (None, None)
	min2 = (None, None)
	min1i = None
	min2i = None

	for i in range(0, len(leafs)):
		if min1 == (None, None):
			min1 = leafs[i].val
			min1i = i
		else:
			if (leafs[i].val)[1]<=min1[1]:
				min1 = leafs[i].val
				min1i = i
	
	for i in range(0, len(leafs)):
		if leafs[i].val != min1:
			if min2 == (None, None):
				min2 = leafs[i].val
				min2i = i
			else:
				if (leafs[i].val)[1]<=min2[1]:
					min2 = leafs[i].val
					min2i = i

	nodeToAdd = node(leafs[min1i], (min1[0]+min2[0], min1[1]+min2[1]) ,leafs[min2i])

	newLeafs = []

	for leaf in leafs:
		if leaf.val != min1 and leaf.val != min2:
			newLeafs += [leaf]

	newLeafs += [nodeToAdd]

	return buildHuffmanCompressionTree(newLeafs)

def buildKeyFromTree(root, s=""):
	if root.left == None and root.right == None:
		d = {}
		d[root.val[0]] = s
		return d
	k = {}
	if root.left:
		k = dict(k.items() + (buildKeyFromTree(root.left, "0"+s)).items())
	if root.right:
		k = dict(k.items() + (buildKeyFromTree(root.right, "1"+s)).items())
	return k

def huffmanCompression(s):
	charCount = {}
	for c in s:
		if charCount.has_key(c):
			charCount[c] += 1
		else:
			charCount[c] = 1
	leafs = []
	for tup in charCount.items():
		leafs += [node(None, tup, None)]
	root = buildHuffmanCompressionTree(leafs)
	key = buildKeyFromTree(root)
	rep = ""
	for c in s:
		rep += key[c]
	return (rep, key)
	





print "------------ RESULT ------------"
print "Your Message: %s" % m
normal = stringToBits(m)
print "8 Bits Rep.: %s" % normal
compressed, key =huffmanCompression(m)
print "Compressed : %s" % compressed
print "Key for Uncompression: %s" % key
print "Space saved: ~ %s" % str(100 - float(len(compressed))/float(len(normal))*100)+" %"
# print "# of bits for 8 Bits Rep.: %i" % len(stringToBits(m))
print "--------------------------------"
# print intToBits(10)

# print "Normal Bits: %s" % string(m
