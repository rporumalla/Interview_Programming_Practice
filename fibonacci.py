def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

def F():
  a,b=0,1
  yield a
  yield b
  while True:
    a,b=b,a+b
    yield b

def fibRange(start,end):
  for cur in F():
    if cur>end: return
    if cur>=start: yield cur

n=10
for i in range(n):
  print fibonacci(i),
print
i=0

# Fibonacci Series less than a particular value
curr=fibonacci(i)
while curr<=200:
  print curr,
  i+=1
  curr=fibonacci(i)

# Display startNumber to endNumber only from Fib sequence
for i in fibRange(10,200):
  print i
