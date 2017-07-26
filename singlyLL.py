
class Node(object):
  def __init__(self,data):
    self.data=data
    self.next=None

  def __str__(self):
    return str(self.__dict__)

#  def __eq__(self,other):
#    return self.__dict__ == other.__dict__

class SingleList(object):
  def __init__(self):
    self.head=None
    self.tail=None

  def count(self):
    length=0
    current=self.head
    while current is not None:
      length+=1
      current=current.next
    return length

  # add node at the end
  def append(self,data):
    node=Node(data)
    if self.head is None:
      self.head=self.tail=node
    else:
      self.tail.next=node
    self.tail=node

  # add node at the beginning
  def append1(self,data):
    current=self.head
    node=Node(data)
    if current is not None:
      self.head=node
      self.head.next=current
    else:
      self.head=self.tail=node

  # add node at a position
  def append2(self,data,pos):
    len=self.count()
    i=0
    node=Node(data)
    current=self.head
    if pos<len:
      if pos==0:
        self.head=node
 	self.heaad.next=current
      else:
	while i<len:
	  if i+1==pos:
	    node.next=current.next
	    current.next=node
	    return self.head
	  current=current.next
	  i+=1
    else:
      print 'Node not inserted'
    return head

  def remove2(self,pos):
    len=self.count()
    i=0
    temp=None
    if pos<len:
      current=self.head
      if pos==0:
	self.head=current.next
      else:
	while i<len:
	  if i+1 == pos:
	    temp=current.next
 	    current.next=temp.next
	    return True
 	  current=current.next
	  i+=1
    return False

  def remove(self,data):
    current=self.head
    previous=None
    while current is not None:
      if current.data==data:
	if previous is not None:
	  previous.next=current.next
	else:
	  self.head=current.next
      previous=current
      current=current.next

  def checkAndRemoveLoop(self):
    first=self.head
    second=self.head.next
    while first and second and second.next:
      if first==second:
	print 'Cycle Exists'
	break
      first=first.next
      second=second.next.next
    # if loop exists
    if first==second:
      first=self.head
      while first !=second.next:
	first=first.next
	second=second.next
      second.next=None # remove loop
      return first
    print 'No Cycle Exists'
    return self.head

  def show(self):
    current=self.head
    while current is not None:
      print current.data,'->',
      current=current.next
    print None

s=SingleList()
s.append(31)
s.append(2)
s.append(3)
s.append(4)
s.show()
s.append2(8,2)
s.show()
print s.checkAndRemoveLoop()
s.remove2(2)
s.show()
s.remove(31)
s.remove(3)
s.show()
s.remove(2)
s.show()
s1=SingleList()
s1.append(10)
s1.append(4)
s1.append(15)
s1.append(20)
s1.append(50)
s1.head.next.next.next.next.next=s1.head.next.next
#s1.show()
print s1.checkAndRemoveLoop()
s1.show()
s2=SingleList()
s2.append('a')
s2.append('b')
s2.append('c')
s2.append('d')
s2.append('e')
s2.append('f')
s2.append('g')
s2.append('h')
s2.append('i')
s2.append('j')
s2.head.next.next.next.next.next.next.next.next.next.next=s2.head.next.next
#s2.show()
print s2.checkAndRemoveLoop()
s2.show()
