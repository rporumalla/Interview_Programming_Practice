def isAnagram(s1,s2):
  l1=len(s1)
  l2=len(s2)
  if l1!=l2:
    return False
  for i in range(l1):
    j=0
    found=False
    while j<l2:
      if s1[i]==s2[j]:
        found=True
        break
      j+=1
    if not found:
      break
  return found

print isAnagram('abcd','dcba')
print isAnagram('abcd','dcbc')
print isAnagram('iceman','cinema')
