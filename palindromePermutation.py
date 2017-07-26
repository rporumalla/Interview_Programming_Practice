def getCharNumber(c):
  a=ord('a')
  z=ord('z')
  v=ord(c)
  if v>=a and v<=z:
    return v-a
  return -1

def isPermutationOfPalindrome(s):
  s=s.lower()
  countOdd=0
  table=[0]*26
  for c in s:
    x=getCharNumber(c)
    #print 'x:',x
    if x!=-1:
      table[x]+=1
      if table[x]%2==1:
	countOdd+=1
      else:
	countOdd-=1
  return countOdd<2

print isPermutationOfPalindrome('Tact Coa')
print isPermutationOfPalindrome('Tact Cot')
