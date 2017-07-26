class Queue:
  def __init__(self):
    self.items=[]

  def isEmpty(self):
    return self.items==[]

  def size(self):
    return len(self.items)

  def enqueue(self,item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

#  def __str_(self):
#    return str(self.__dict__)   

class Stack:
  def __init__(self):
    self.q1=Queue()
    self.q2=Queue()

  def push(self,item):
    self.q1.enqueue(item)

  def pop(self):
    size=self.q1.size()
    if size==1:
      x=self.q1.dequeue()
    elif size>1:
      for i in range(size-1):
	self.q2.enqueue(self.q1.dequeue())
      x=self.q1.dequeue()
      temp=self.q1
      self.q1=self.q2
      self.q2=temp
    else:
      x=None
    return x 

s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
s1.push(9)
s1.push(10)
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
