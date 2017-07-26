# O(log n)
def binarySearch(myList,x):
  myList=sorted(myList)
  low=0
  high=len(myList)-1
  while True:
    if low>high:
      return -1
    mid=low+(high-low)/2
    if x<myList[mid]:
      high=mid-1
    elif x>myList[mid]:
      low=mid+1
    else:
      return mid

lst=[10,14,19,26,27,31,33,35,42,44]
idx=binarySearch(lst,31)
if idx==-1:
  print 'Number not found'
else:
  print 'Number found at index ', idx

idx=binarySearch(lst,32)
if idx==-1:
  print 'Number not found'
else:
  print 'Number found at index ', idx
