# O(n)
def twoSum(myList,n):
  hm={}
  lst=[]
  if myList is None or len(myList)<2:
    lst.append((0,0))
  else:
    for i in range(len(myList)):
      if myList[i] in hm:
	lst.append((hm[myList[i]],myList[i]))
      else:		
        hm[n-myList[i]]=myList[i]
  return lst

lst=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print twoSum(lst,10)
