def window(s1,s2):
  l=len(s2)
  it=iter(s1)
  w=[]
  for i in range(l):
    w.append(next(it))
  yield w
  for i in it:
    w=w[1:]+[i]
    yield w

def isSubStr1(s1,s2):
  l1=window(s1,s2)
  l2=list(s2)
  for x in l1:
    if x==l2:
      return True
  return False
 

print isSubStr1('abcdef','bcd')
print isSubStr1('aacqsd','qd')
print isSubStr1('abcd','abcd')
print isSubStr1('aaaa','a')
print isSubStr1('abcdefghi','ghi')
print isSubStr1('abcdef','fe')
