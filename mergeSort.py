# O(nlog n) - best/avg/worst time complexity
# O(n) space complexity
# Divide and Conquer Algorithm

def mergeSort(lst,start,end):
  if start<end:
    mid=start+(end-start)/2
    mergeSort(lst,start,mid)
    mergeSort(lst,mid+1,end)
    merge(lst,start,mid,end)

def merge(lst,start,mid,end):
    print 'start:',start
    print 'end:',end
    print 'mid:',mid
    n1,n2=mid-start+1,end-mid
    left=[0]*n1
    right=[0]*n2
    for i in range(n1):
      left[i]=lst[start+i]
    for j in range(n2):
      right[j]=lst[mid+1+j]
    i,j,k=0,0,start
    while i<n1 and j<n2:
      if left[i]<=right[j]:
        lst[k]=left[i]
        i+=1
      else:
        lst[k]=right[j]
        j+=1
      k+=1
    while i<n1:
      lst[k]=left[i]
      i+=1
      k+=1
    while j<n2:
      lst[k]=right[j]
      j+=1
      k+=1

alist=[12, 11, 13, 5, 6, 7]
mergeSort(alist,0,len(alist)-1)
print alist

alist=[7, 2, 1, 8, 6, 3, 5, 4]
mergeSort(alist,0,len(alist)-1)
print alist

alist=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(alist,0,len(alist)-1)
print alist

alist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mergeSort(alist,0,len(alist)-1)
print alist

alist=[1, 6, 2, 7, 3, 8, 4, 9, 5]
mergeSort(alist,0,len(alist)-1)
print alist
