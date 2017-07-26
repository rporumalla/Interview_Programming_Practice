#import textwrap
from Queue import Queue
import sys

MIN_VALUE=-sys.maxint-1

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

class Tree:
    def __init__(self, node):
        self.root = node

    def lookup(self, node, target):
        if node:
            if target == node.data:
                return True
            elif target < node.data and node.left is not None:
                return self.lookup(node.left, target)
            elif target > node.data and node.right is not None:
                return self.lookup(node.right, target)
        else:
            return False

    def insert(self, node, val):
        if not node:
            return Node(val)
        else:
            if val <= node.data:
                node.left = self.insert(node.left, val)
            else:
                node.right = self.insert(node.right, val)

            #return node

    def build123a(self):
        root = Node(2)
        child1 = Node(1)
        child2 = Node(3)
        root.left = child1
        root.right = child2

    def build123b(self):
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)

    def build123c(self):
        root = None
        self.insert(root, 2)
        self.insert(root, 1)
        self.insert(root, 3)

    # Computes the number of nodes in tree
    # O(n)
    def size(self, node):
	# Size = 1 (for the root) + Size Of left Sub-Tree + Size Of right Sub-Tree
        if node:
            return self.size(node.left) + 1 + self.size(node.right)
        else:
            return 0

    # O(n)
    # In the average case, for a balanced binary tree
    # T(n) = 2T(n/2) + Θ(1);
    # Every recursive call gives you two problems of half the size. By master theorem, this would evaluate to T(n) = Θ(n)
    # In the worst case, where each node has only one child.
    # T(n) = T(n-1) + Θ(1)
    # Which evaluates to T(n) = Θ(n)
    def getHeight(self, node):
	if node is None:
	    return -1
	return max(self.getHeight(node.left),self.getHeight(self.right))+1

    def maxDepth(self, node):
        if node:
            lheight = self.maxDepth(node.left)
            rheight = self.maxDepth(node.right)
            return 1 + max(lheight, rheight)
        else:
            return 0

    # O(n logn)
    def isBalanced1(self, node):
	if node is None:
	    return True
	height_diff=self.getHeight(node.left)-self.getHeight(node.right)
	if abs(height_diff)>1:
	    return False
	else:
	    return self.isBalanced1(node.left) and self.isBalanced1(self.right)

    def checkHeight(self, node):
	if node is None:
	    return -1
	left_height = self.checkHeight(node.left)
	if left_height == MIN_VALUE:
	    return MIN_VALUE
	right_height = self.checkHeight(node.right)
	if right_height == MIN_VALUE:
	    return MIN_VALUE
	height_diff=left_height-right_height
	if abs(height_diff)>1:
	    return MIN_VALUE
	else:
	    return max(left_height,right_height)+1

    # O(n) time and O(h) space, where h is height of the tree
    def isBalanced2(self, node):
	return self.checkHeight(node) != MIN_VALUE

    def minValue(self, node):
        while node.left:
            current = node.left

        return current.data

    def deleteTree(self):
        self.root = None

    def printInorder(self, node):
        if node:
            self.printInorder(node.left)
            print node,
            self.printInorder(node.right)
        else:
            return None

    def printPostorder(self, node):
        if node:
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print node,
        else:
            return None

    """
        PreOrder Traversal
    """
    def printCurrentNodeInTree(self, node, current, comment='*', level=0):
        if node:
            if node == current:
                print '\t' * level + node + comment
            else:
                print '\t' * level + node

            self.printCurrentNodeInTree(node.left, current, comment, level+1)
            self.printCurrentNodeInTree(node.right, current, comment, level+1)
        else:
            return None

    def preOrder(self, node):
        if node:
            self.printCurrentNodeInTree(self.root, node)
            self.preOrder(node.left)
            self.preOrder(node.right)
        else:
            return None

    def levelOrder(self):
        q = Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print node,
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def printLevelOrder(self):
        h = self.maxDepth(self.root)

        for i in range(h):
            self.printGivenLevel(self.root, i)
            print '\n'

    def printGivenLevel(self, node, level):
        if node:
            if level == 0:
                print node,
            elif level > 0:
                self.printGivenLevel(node.left, level-1)
                self.printGivenLevel(node.right, level-1)

def treeCompare(node1, node2):
    # if node1 == node2:
    #     return True
    if node1 is None and node2 is None:
        return True

    return node1 == node2 and treeCompare(node1.left, node2.left) and \
               treeCompare(node1.right, node2.right)
    return False

a = Node(5)
b = Node(5)
c = Node(5)
tree = Tree(a)
tree1 = Tree(b)
tree2 = Tree(c)
tree.insert(a, 9)
tree1.insert(b, 9)
tree2.insert(c, 9)
tree.insert(a, 6)
tree1.insert(b, 6)
tree2.insert(c, 6)
tree.insert(a, 3)
tree1.insert(b, 3)
tree2.insert(c, 3)
tree.insert(a, 4)
tree1.insert(b, 4)
tree2.insert(c, 4)
tree.insert(a, 1)
tree1.insert(b, 1)
tree2.insert(c, 2)

#tree.printInorder(a)
#d = Node(5)
#tree.printCurrentNodeInTree(a,d)
#tree.printPostorder(a)
#tree.preOrder(a)
#tree.levelOrder()
tree.printLevelOrder()
print "**************"
tree1.printLevelOrder()
if treeCompare(tree.root, tree1.root):
    print "same binary trees"
else:
    print "different binary trees"

if treeCompare(tree.root, tree2.root):
    print "same binary trees"
else:
    print "different binary trees"
