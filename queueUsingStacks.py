class Stack:
  def __init__(self):
    self.elements=[]

  def push(self,item):
    self.elements.append(item)

  def pop(self):
    return self.elements.pop()

  def peek(self):
    return self.elements[-1]

  def size(self):
    return len(self.elements)

  def isEmpty(self):
    return self.size()==0

class MyQueue:
  def __init__(self):
    self.stack1=Stack()
    self.stack2=Stack()

  def enqueue(self,item):
    self.stack1.push(item)

  def dequeue(self):
    if self.stack1.isEmpty() and self.stack2.isEmpty():
      print 'Queue is Empty'
      return None
    if self.stack2.isEmpty():
      while not self.stack1.isEmpty():
        self.stack2.push(self.stack1.pop())
    x=self.stack2.pop()
    return x

q1=MyQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print q1.dequeue()
print q1.dequeue()
print q1.dequeue()
print q1.dequeue()
