def reverse(s):
  l=len(s)
  t=''
  for i in range(l-1,-1,-1):
    t+=s[i]

  return t

a=123
print reverse(str(a))
print str(a)==reverse(str(a))
a='kayak'
print reverse(str(a))
print a==reverse(a)
a=121
print str(a)==reverse(str(a))
a='quick brown fox'
print reverse(str(a))
print a==reverse(str(a))
