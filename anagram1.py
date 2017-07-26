def isAnagram(s1,s2):
  l1=sorted(s1)
  l2=sorted(s2)
  
  if l1==l2:
    return True
  return False

print isAnagram('abcd','dcba')
print isAnagram('abcd','dcbc')
print isAnagram('iceman','cinema')
