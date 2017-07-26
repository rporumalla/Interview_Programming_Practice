def reverse(v):
  reversed=0
  while v!=0:
    reversed=reversed*10+v%10
    v=v/10
  return reversed

a=1234
print reverse(a)
print a==reverse(a)
a=1221
print a==reverse(a)
