#! python

'''def isUniqueChars(str):
 if len(str) > 128:
  return False

 char_set = [0]*256

 for c in str:
  if char_set[ord(c)] != 0:
   return False
  else:
   char_set[ord(c)] = 1

 return True
'''
def isUniqueChars2(str):
 checker = 0

 for c in str:
  val = ord(c) - ord('a')
  if (checker & (1 << val)) > 0:
   return False
  else:
   checker |= (1 << val)
 return True

