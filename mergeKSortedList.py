class ListNode(object):
  def __init__(self,data):
    self.data=data
    self.next=None

  def __repr__(self):
    if self:
      return "{} -> {}".format(self.data,self.next)

class Solution(object):
  def mergeKLists(self,lists):
    if len(lists)==0:
      return None
    while len(lists)>1:
      temp=[]
      for i in range(0,len(lists)-1,2):
        temp.append(self.merge2Lists(lists[i],lists[i+1]))
      if len(lists)%2==1:
	temp.append(lists[len(lists)-1])
      lists=temp
    return lists[0]

  def merge2Lists(self,list1,list2):
    dummy=list=ListNode(0)
    while list1 and list2:
      if list1.data<list2.data:
	list.next=list1
	list1=list1.next
      else:
	list.next=list2
	list2=list2.next
      list=list.next
    if list1 is None:
      list.next=list2
    else:
      list.next=list1
    return dummy.next

if __name__=="__main__":
  l1=ListNode(1)
  l1.next=ListNode(3)
  l2=ListNode(2)
  l2.next=ListNode(5)
  l3=ListNode(3)
  l3.next=ListNode(6)

  print Solution().mergeKLists([l1,l2,l3])
