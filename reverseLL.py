# Time Complexity: O(n)
# Space Complexity: O(1)
# add nodes at beginning
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class linkedList:
  def __init__(self):
    self.head=None

  def push(self,new_data):
    node=Node(new_data)
    node.next=self.head
    self.head=node

  def reverse(self):
    current=self.head
    prev=None
    while current is not None:
      temp = current.next
      current.next=prev
      prev=current
      current=temp
    self.head=prev

  def printList(self):
    current=self.head
    while current is not None:
      print current.data,'->',
      current=current.next

ll=linkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)

print 'linked list:'
ll.printList()
ll.reverse()
print '\nreversed list:'
ll.printList()
