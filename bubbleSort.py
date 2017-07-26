# O(n^2) time complexity O(n) best time complexity
# O(1) space complexity
def bubbleSort(lst):
  exchanges=True
  passes=len(lst)-1
  while exchanges and passes>0:
    exchanges=False
    for i in range(passes):
      if lst[i]>lst[i+1]:
	lst[i],lst[i+1]=lst[i+1],lst[i]
	exchanges=True
    passes-=1

alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSort(alist)
print alist
alist=[100,90,80,70,60,50,40,30,20,-10,10,0]
bubbleSort(alist)
print alist
