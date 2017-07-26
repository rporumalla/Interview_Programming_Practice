def numOnebits(n):
  count=0
  while n:
    count+=n&1
    n=n>>1
  return count

print numOnebits(15)
print numOnebits(9)
