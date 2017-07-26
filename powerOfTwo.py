def isPowerOfTwo(n):
  if n<=0:
    return False
  while n>2:
    a=n>>1
    b=a<<1
 
    if b-n!=0:
      return False
    n=n>>1
  return True

if __name__=='__main__':
  print isPowerOfTwo(2)
  print isPowerOfTwo(1)
  print isPowerOfTwo(5)
  print isPowerOfTwo(4)
  print isPowerOfTwo(6)
  print isPowerOfTwo(16)
  print isPowerOfTwo(-4)
