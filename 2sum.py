def twoSum(myList,n):
  myList=sorted(myList)
  #myList=list(set(myList))
  i=0
  j=len(myList)-1
  ltups=[]
  #temp=0
  while i<j:
    if myList[i]+myList[j]==n:
      ltups.append((myList[i],myList[j]))
      i+=1
      #temp=j
    elif myList[i]+myList[j]>n:
      j-=1
    else:
      i+=1
  return ltups

lst=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print twoSum(lst,10)
lst=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
print twoSum(lst,10)
