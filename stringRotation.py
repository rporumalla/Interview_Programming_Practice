def isRotation(s1,s2):
  if len(s1)!=len(s2):
    return False
  if len(s1)>0:
    s=s1+s1
    if s.find(s2)>0:
      return True
  return False

print isRotation("waterbottle","erbottlewat")
print isRotation("waterbottle","erbottlewet")
print isRotation("waterbottle","erbottlewater")
