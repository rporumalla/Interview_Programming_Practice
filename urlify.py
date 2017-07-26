def replaceSpaces(s,l):
  count=0
  for c in s:
    if c==' ':
      count+=1
  idx=l+2*count
  ns=['']*idx
  while idx-1>=0 and l-1>=0:
    idx-=1
    l-=1
    if s[l]==' ':
      ns[idx]='0'
      ns[idx-1]='2'
      ns[idx-2]='%'
      idx-=2
    else:
      ns[idx]=s[l]
  return ''.join(ns)

print replaceSpaces("Mr John Smith ", 13)
