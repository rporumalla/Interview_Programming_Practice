def factors(n):
  a=[]
  for i in range(1,n+1):
    if n%i==0:
      a.append(i)
  return a

print factors(20)
print factors(120)
print factors(57)
