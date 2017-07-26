# O(n^2) avg/worst O(n) best time complexity
# O(1) space complexity
def insertionSort(lst):
  for i in range(1,len(lst)):
    pos=i
    curr=lst[i]
    while pos>0 and lst[pos-1]>curr:
      lst[pos]=lst[pos-1]
      pos-=1
    lst[pos]=curr

alist=[54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print alist
