def numPaths(m,n):
  global N
  if m==1 or n==N:
    return 1
  return numPaths(m-1,n)+numPaths(m,n+1)

N=10
print numPaths(N,1)
