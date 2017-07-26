# O(m+n) where m and n are the sizes of given two linked lists
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None

  def push(self,data):
    node=Node(data)
    node.next=self.head
    self.head=node

  def pop(self):
    if self.head:
      temp=self.head
      self.head=temp.next
      return temp 

  def printList(self):
    node=self.head 
    while node is not None:
      print node.data, '->',
      node=node.next

  def addTwoLists(self,first,second):
    carry=0
    prev=None
    while first is not None or second is not None:
      fdata=0 if first is None else first.data 
      sdata=0 if second is None else second.data
      sum=fdata+sdata+carry
      if sum>9:
	carry=sum/10
      else:
	carry=0
      sum=sum%10
      temp=Node(sum)
      if self.head is None:
	self.head=temp
      else:
	prev.next=temp
      prev=temp
      if first:
	first=first.next
      if second:
	second=second.next

l1=LinkedList()
l2=LinkedList()
l1.push(6)
l1.push(4)
l1.push(9)
l1.push(5)
l1.push(7)
print 'First List:'
l1.printList()
l2.push(4)
l2.push(8)
print '\nSecond List:'
l2.printList()
res=LinkedList()
res.addTwoLists(l1.head,l2.head)
print '\nNew List:'
res.printList()
