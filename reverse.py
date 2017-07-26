def reverse(s):
  if len(s)<2:
    return s
  return reverse(s[1:]) + s[0]

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
