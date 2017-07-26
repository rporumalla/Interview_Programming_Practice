NOCHARS=256

def getCharCountList(s):
  counts=[0]*NOCHARS
  for c in s:
    counts[ord(c)]+=1
  return counts

def firstNonRepeating(st):
  counts=getCharCountList(st)
  ans=''
  for i in st:
    if counts[ord(i)]==1:
      ans=i
      break
  return ans

t='abcdcbaed'
ans=firstNonRepeating(t)
if ans:
  print 'First non-repeating character is ' + ans
else:
  print 'No non-repeating character'
