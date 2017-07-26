INT_MAX=4294967296
INT_MIN=-4294967296

class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

class BinaryTree:
  prev=None
  def __init__(self,node):
    self.root=node

  # O(n)
  # In-Order Traversal
  def isBst(self,node):
    if node:
      if not self.isBst(node.left):
        return False
      if BinaryTree.prev and node.data<BinaryTree.prev.data:
        return False
      BinaryTree.prev=node
      return self.isBst(node.right)
    return True

  # O(n)
  def isBst1(self, node):
    return self.isBstUtil(node,INT_MIN,INT_MAX)

  def isBstUtil(self,node,mini,maxi):
    if node is None:
      return True
    if node.data<mini or node.data>maxi:
      return False
    return (self.isBstUtil(node.left,mini,node.data-1)) and (self.isBstUtil(node.right,node.data+1,maxi))

root=Node(4)
tree=BinaryTree(root)
tree.root.left=Node(2)
tree.root.right=Node(5)
tree.root.left.left=Node(1)
tree.root.left.right=Node(3)
if tree.isBst(tree.root):
  print "BST"
else:
  print "Not a BST"
if tree.isBst1(tree.root):
  print "BST"
else:
  print "Not a BST"
