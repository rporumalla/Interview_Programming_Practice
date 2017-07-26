# O(n)
def maxContSum(myList):
  a=myList[0]
  b=myList[0]
  for i in range(1,len(myList)):
    a=max(myList[i],myList[i]+a)
    b=max(b,a)
  return b

lst=[1, 2, -4, 1, 3, -2, 3, -1]
print maxContSum(lst)

lst=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxContSum(lst)
