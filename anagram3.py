def window(s,size):
  s=list(s)
  it=iter(s)
  w=[]
  for i in range(size):
    w.append(next(it)) 
  yield w
  for i in it:
    w=w[1:]+[i]
    yield w

def isAnagram(s1,s2):
  l1=len(s1)
  l2=len(s2)
  print 's1:', s1
  print 's2:', s2
  d={}
  for c in s2:
    if c in d:
      d[c]+=1
    else:
      d[c]=1
  w=window(s1,l2)
  print w
  for e in w:
    print 'e:',e
    if all(i in e for i in d):
      c=d.copy()
      print c
      for i in e:
        if i in c:
          c[i]-=1
      if all(v==0 for v in c.values()):
	return True
  return False

print isAnagram('abcd','dcba')
print isAnagram('abcd','dcbc')
print isAnagram('iceman','cinema')
print isAnagram('axweqicemanui','cinema')
