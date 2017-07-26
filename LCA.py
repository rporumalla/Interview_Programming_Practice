# O(n)
class Node:
  def __init__(self,key):
    self.key=key
    self.left=None
    self.right=None

def findPath(root,path,n):
  if not root:
    return False
  path.append(root.key)
  if root.key==n:
    return True
  if (root.left and findPath(root.left,path,n)) or (root.right and findPath(root.right,path,n)):
    return True
  print 'pop:',path.pop()
  return False

def findLCA(root,n1,n2):
  path1=[]
  path2=[]
  if not findPath(root,path1,n1) or not findPath(root,path2,n2):
    return -1
  i=0
  print 'path1:',path1
  print 'path2:', path2
  while i<len(path1) and i<len(path2):
    if path1[i]!=path2[i]:
      break
    i+=1
  return path1[i-1]

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print findLCA(root,4,5)
print findLCA(root,4,6)
print findLCA(root,3,4)
print findLCA(root,2,4)
print findLCA(root,4,8)
