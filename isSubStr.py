def isSubStr(s1,s2):
  l1=len(s1)
  l2=len(s2)
  for i in range(l1-l2+1):
    s=s1[i:i+l2]
    print s
    if s==s2:
      return True
  return False

print isSubStr('abcdef','bcd')
print isSubStr('aacqsd','qd')
print isSubStr('abcd','abcd')
print isSubStr('aaaa','a')
print isSubStr('abcdefghi','ghi')
print isSubStr('abcdef','fe')
