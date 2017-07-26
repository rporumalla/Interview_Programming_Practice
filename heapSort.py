# O(nlog n) - Best/Avg/Worst Time Complexity
# O(1) - Space Complexity
def buildMaxHeap(lst):
  for i in range(len(lst),-1,-1):
    heapify(lst,len(lst),i)
  print '-----------------'

def heapify(lst,n,i):
  largest=i
  left=2*i+1
  right=2*i+2
  print 'left:',left
  print 'right:',right
  print 'largest:',largest
  print 'n:',n
  if left<n and lst[left]>lst[largest]:
    largest=left
  if right<n and lst[right]>lst[largest]:
    largest=right
  print 'largest1:',largest
  if largest!=i:
    lst[largest],lst[i]=lst[i],lst[largest]
    heapify(lst,n,largest)

def heapSort(lst):
  buildMaxHeap(lst)
  for i in range(len(lst)-1,0,-1):
    lst[i],lst[0]=lst[0],lst[i]
    heapify(lst,i,0)

lst=[ 12, 11, 13, 5, 6, 7]
heapSort(lst)
print lst

lst=[3,4,8,9,7,10,9,15,20,13]
heapSort(lst)
print lst
