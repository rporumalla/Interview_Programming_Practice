# O(n)
def minmax(myList, low, high):
  if low==high:
    min=myList[low]
    max=myList[low]
    return (min,max)
  elif high==low+1:
    if myList[high]>myList[low]:
      min=myList[low]
      max=myList[high]
    else:
      min=myList[high]
      max=myList[low]
    return (min,max)
  else:
    mid=low+(high-low)/2
    min1,max1=minmax(myList,low,mid)
    min2,max2=minmax(myList,mid+1,high)
  if min1<min2:
    min=min1
  else:
    min=min2
  if max1>max2:
    max=max1
  else:
    max=max2
  return (min,max)

lst=[7, 2, 1, 8, 6, 3, 5, 4]
x,y=minmax(lst,0,len(lst)-1)
print x, y

lst=[1000, 11, 445, 1, 330, 3000, -1]
x,y=minmax(lst,0,len(lst)-1)
print x, y
