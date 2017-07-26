def absolute(n):
  mask=n>>31
  return (n^mask)-mask

print absolute(-99)
print absolute(-71)
