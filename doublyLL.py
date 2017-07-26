class Node(object):
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

class DoubleList(object):
  def __init__(self):
    self.head=None
    self.tail=None

  def append(self,data):
    node=Node(data)
    if self.head is None:
      self.head=self.tail=node
    else:
      self.tail.next=node
      node.prev=self.tail
      self.tail=node

  def remove(self,data):     
    current=self.head
    while current is not None:
      if current.data==data:
	if current.prev is not None:
	  current.prev.next=current.next
          current.next.prev=current.prev
	else:
	  self.head=current.next
	  self.head.prev=None
      current=current.next

  def show(self):
    current=self.head
    while current is not None:
      print current.prev.data if hasattr(current.prev,'data') else None
      print current.data,
      print current.next.data if hasattr(current.next,'data') else None
      current=current.next
    print '*'*50

d=DoubleList()
d.append(5)
d.append(6)
d.append(50)
d.append(30)
d.show()
d.remove(50)
d.remove(5)
d.show()
