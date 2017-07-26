# best/avg time complexity - O(n log n)
# worst time complexity - O(n**2)
# worst space complexity - O(log n)
# Divide and Conquer Algorithm

#we can attempt to alleviate some of the potential for an uneven division by using a technique called median of three.
#To choose the pivot value, we will consider the first, the middle, and the last element in the list.
#To analyze the quickSort function, note that for a list of length n, if the partition always occurs in the middle of the list,

def quicksort(myList, start, end):
  if start<end:
    pivot=partition(myList,start,end)
    quicksort(myList,start,pivot-1)
    quicksort(myList,pivot+1,end)
  return myList

def partition(myList, start, end):
  pivot=myList[end]
  i=start-1
  j=i+1
  while j<end:
    if myList[j]<pivot:
      i+=1
      if i!=j:
	myList[i],myList[j]=myList[j],myList[i]
    j+=1
  myList[i+1],myList[end]=pivot,myList[i+1]
  return i+1

lst=[7, 2, 1, 8, 6, 3, 5, 4]
quicksort(lst,0,len(lst)-1)
print ' '.join(str(e) for e in lst)

lst=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quicksort(lst,0,len(lst)-1)
print ' '.join(str(e) for e in lst)

lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quicksort(lst,0,len(lst)-1)
print ' '.join(str(e) for e in lst)

lst=[1, 6, 2, 7, 3, 8, 4, 9, 5]
quicksort(lst,0,len(lst)-1)
print ' '.join(str(e) for e in lst)

lst=[12, 11, 13, 5, 6, 7]
quicksort(lst,0,len(lst)-1)
print ' '.join(str(e) for e in lst)
