import math

# Sieve of Eratosthenes - Find n prime numbers
# O(nloglog n)
def primeNumbers(n):
  primes=[]
  for i in range(n):
    primes.append(1)
  primes.insert(0,0)
  primes.insert(1,0)
  for i in range(2,int(math.sqrt(n))): 
    for j in range(2,n):
      #if i*j>n:
	#break
      if primes[j]==1:
        primes.insert(i*j,0)
  return [i for i,j in enumerate(primes) if j==1]

print primeNumbers(20)
