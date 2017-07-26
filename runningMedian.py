from heapq import heappush, heappop

class Heap:
  def __init__(self):
    self.max_heap=[]
    self.min_heap=[]

  def addNum(self,num):
    l=len(self.max_heap)
    r=len(self.min_heap)
    if l==0 and r==0:
      heappush(self.min_heap,num)
      return
    if self.max_heap:
      lval=-self.max_heap[0]
    if self.min_heap:
      rval=self.min_heap[0]
    if l==r:
      if num<=lval:
	heappush(self.max_heap,-num)
      else:
	heappush(self.min_heap,num)
    elif l>r:
      if num>=lval:
	heappush(self.min_heap,num)
      else:
	tmp=heappop(self.max_heap)
	heappush(self.min_heap,-tmp)
	heappush(self.max_heap,-num)
    else:
      if num<rval:
	heappush(self.max_heap,-num)
      else:
	tmp=heappop(self.min_heap)
	heappush(self.min_heap,num)
	heappush(self.max_heap,-tmp)

  def findMedian(self):
    l=len(self.max_heap)
    r=len(self.min_heap)
    print 'max_heap:',self.max_heap
    print 'min_heap:',self.min_heap
    if l==r:
      return (self.min_heap[0]-self.max_heap[0])/2.0
    elif l>r:
      return float(-self.max_heap[0])
    else:
      return float(self.min_heap[0])

h=Heap()
lst=[3,4,8,9,7,10,9,15,20,13]
for num in lst:
  h.addNum(num)
print h.findMedian()

h1=Heap()
lst=[1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for num in lst:
  h1.addNum(num)
print h1.findMedian()
