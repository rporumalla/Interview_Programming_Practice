def gcd(a,b):
  while b>0:
    a,b=b,a%b
  return a

def lcm(a,b):
  print 'gcd: ', gcd(a,b)
  return a*b/gcd(a,b)

print lcm(8,12)
print lcm(100,75)
