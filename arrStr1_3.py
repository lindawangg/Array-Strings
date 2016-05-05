#! python

def sort(string):
	return ''.join(sorted(string))

def permutation(string1, string2):
	if len(string1) == len(string2):
		return sorted(string1) == sorted(string2)
	return False