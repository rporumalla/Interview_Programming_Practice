# O(n)
def minmax(myList):
  l=len(myList)
  if l==1:
    min=myList[0]
    max=myList[0]
    return (min,max)

  if myList[0]<myList[1]:
    min=myList[0]
    max=myList[1]
  else:
    min=myList[1]
    max=myList[0]

  for i in range(2,l):
    if myList[i]<min:
      min=myList[i]
    if myList[i]>max:
      max=myList[i]
  return (min,max) 

lst=[7, 2, 1, 8, 6, 3, 5, 4]
x,y=minmax(lst)
print x, y

lst=[1000, 11, 445, 1, 330, 3000, -1]
x,y=minmax(lst)
print x, y
