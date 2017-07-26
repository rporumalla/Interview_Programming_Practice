def dupes(lst):
  d1={}
  d2=[]
  for i in range(len(lst)):
    if lst[i] in d1 and lst[i] not in d2:
      d2.append(lst[i])
    else:
      d1[lst[i]]=1
  return d2

a=[0,1,2,3,2]
print dupes(a)
