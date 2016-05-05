#! python 

def countCompression(str1):
	if len(str1)==0:
		return 0
	last = str1[0]
	size = 0
	count = 1
	for c in str1:
		if c == last:
			count = count + 1
		else:
			last = c
			size = size + 1 + len(str(count))
			count = 1
	size = size + 1 + len(str(count))
	return size 


def compress(str1):
	#Check if compression will create a longer string
	size = countCompression(str1)
	if size >= len(str1):
		return str1
	last = str1[0]
	count = 1
	newStr = ''
	for c in str1:
		if c == last:
			count = count + 1
		else:
			newStr = newStr + last
			newStr = newStr + str(count)
			last = c
			count = 1
	newStr = newStr + last
	newStr = newStr + str(count)
	return newStr





