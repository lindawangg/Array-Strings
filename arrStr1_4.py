#! python

def replaceSpaces(strArray, length):
	spaceCount = 0
	newLength = 0
	for c in strArray:
		if c == ' ':
			spaceCount = spaceCount + 1
	newLength = length + spaceCount * 2
	newStr = [0]*(newLength+1)
	newStr[newLength] = '\0'
	for s in reversed(strArray):
		if s == ' ':
			newStr[newLength - 1] = '0'	
			newStr[newLength - 2] = '2'
			newStr[newLength - 3] = '%'
			newLength = newLength - 3
		else:
			newStr[newLength - 1] = s
			newLength = newLength - 1
	return newStr