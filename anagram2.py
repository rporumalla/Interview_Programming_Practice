def isAnagram(s1,s2):
  c1=[0]*26
  c2=[0]*26
  s1=s1.lower()
  s2=s2.lower()
  a=ord('a')
  for i in range(len(s1)):
    c1[ord(s1[i])-a]+=1
  for i in range(len(s2)):
    c2[ord(s2[i])-a]+=1
  if c1==c2:
    return True
  return False

print isAnagram('abcd','dcba')
print isAnagram('abcd','dcbc')
print isAnagram('iceman','cinema')
