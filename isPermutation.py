def isPermutation(s1,s2):
  if len(s1)!=len(s2):
    return False
  letters=[0]*128
  for c in s1:
    letters[ord(c)]+=1
  for c in s2:
    letters[ord(c)]-=1
    if letters[ord(c)]<0:
      return False
  return True

print isPermutation('dog','ogd')
print isPermutation('kayak','kayak')
print isPermutation('rajiv','vijar')
print isPermutation('yahoo','yawho')
print isPermutation('aaww','wwaa')
print isPermutation('phil','pill')
