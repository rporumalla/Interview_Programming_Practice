# O(n^2) avg/best/worst time complexity
# O(1) space complexity
def selectionSort(lst):
  for i in range(len(lst)-1,0,-1):
    maxPos=0
    for j in range(1,i+1):
      if lst[j]>lst[maxPos]:
	maxPos=j
    if maxPos!=j:
      lst[j],lst[maxPos]=lst[maxPos],lst[j]
    
alist=[54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print alist
