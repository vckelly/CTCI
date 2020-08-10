import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'stack_queues')))
from q1 import Queue

class Node(object):
    def __init__(self, data=None):
        self.data = data if data else None
        self.children = []
        self.parent = []
        self.status = 'BLANK'

class BSNode(object):
    def __init__(self, data=None):
        self.data = data 
        self.left = self.right = None


class AVLNode(object):
    def __init__(self, data=None, parent=None):
        self.data = data 
        self.parent = parent
        self.height = 0
        self.left = self.right = None
    
    def nextLarger(self):
        if self.right is not None:
            return self.right.findMin()
        cur = self
        while cur.parent is not None and cur is cur.parent.right:
            cur = cur.parent
        return cur.parent

    def findMin(self):
        if self.left is None and self.right is None:
            return self
        cur = None
        if self.left:
            cur = self.left
            while cur.left is not None:
                cur = cur.left
        else:
            cur = self.right
            while cur.left is not None:
                cur = cur.left
        return cur

    def insert(self, node):
        if node is None:
            return
        if node.data < self.data:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
                else:
                    self.parent.right = self.left or self.right
                    if self.parent.right is not None:
                        self.parent.right.parent = self.parent
                return self
        else:
            s = self.nextLarger()
            self.data, s.data = s.data, self.data
            return s.delete()

class GraphNode(object):
    def __init__(self, data=None, neighbors=[]):
        self.data = data 
        self.neighbors = neighbors 
        self.visited = False
    def visit(self):
        self.visited = True
        return self.data
    def getNeighbors(self):
        return self.neighbors
    def addNeighbor(self, neighbor=None, nList=None):
        if nList:
            for n in nList:
                self.neighbors.append(n)
        if neighbor and neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

class Graph(object):
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes else []
    def getNodes(self):
        return self.nodes

class Tree(object):
    def __init__(self, data=None, rNode=None):
        if rNode:
            self.root = rNode
        else:
            self.root = Node(data)

class BSTree(object):
    def __init__(self, data=None, rNode=None):
        if rNode:
            self.root = rNode
        else:
            self.root = BSNode(data)

    def getHeight(self, node):
        if node.left and node.right:
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        elif node.left and not node.right:
            return self.getHeight(node.left) + 1
        elif node.right and not node.left:
            return self.getHeight(node.right) + 1
        else:
            return 0

    def isBalanced(self, node):
        if not node:
            return True

        flag = True 
        if node.left and node.right:
            if abs(self.getHeight(node.left) - self.getHeight(node.right)) > 1:
                return False
        elif node.left and not node.right:
            flag = False if self.getHeight(node.left) > 1 else True 
        elif node.right and not node.left:
            flag = False if self.getHeight(node.right) > 1 else True

        if flag:
            return self.isBalanced(node.left) and self.isBalanced(node.right)
        else:
            return False

    def printTree(self, node):
        if not node:
            return 
        else:
            print('Val: ' + str(node.data) + '  Height: ' + str(self.getHeight(node)))
            self.printTree(node.left)
            self.printTree(node.right)

class AVLTree(object):
    def __init__(self, data=None, rNode=None):
        if rNode:
            self.root = rNode
        else:
            self.root = AVLNode(data)

    def rebalance(self, node):
        while node:
            self.updateHeight(node)
            if self.getHeight(node.left) >= 2 + self.getHeight(node.right):
                if self.getHeight(node.left.left) >= self.getHeight(node.left.right):
                    self.rRotate(node)
                else:
                    self.lRotate(node.left)
                    self.rRotate(node)
            elif self.getHeight(node.right) >= 2 + self.getHeight(node.left):
                if self.getHeight(node.right.right) >= self.getHeight(node.right.left):
                    self.lRotate(node)
                else:
                    self.rRotate(node.right)
                    self.lRotate(node)
            node = node.parent
            

    def lRotate(self, node):
        parent = node.parent
        newChild = node.right
        if newChild.left:
            node.right = newChild.left
            node.right.parent = node
            self.updateHeight(node.right)
        newChild.left = node
        newChild.parent = parent
        if node == parent.right:
            parent.right = newChild
        else:
            parent.left = newChild
        
        cur = newChild.left
        while cur.parent:
            self.updateHeight(cur)
            cur = cur.parent  

    def rRotate(self, node):
        parent = node.parent
        newChild = node.left
        if newChild.right:
            node.left = newChild.right
            node.left.parent = node
            self.updateHeight(node.left)
        newChild.right = node
        newChild.parent = parent
        if node == parent.right:
            parent.right = newChild
        else:
            parent.left = newChild
        
        cur = newChild.right
        while cur.parent:
            self.updateHeight(cur)
            cur = cur.parent

    def getHeight(self, node):
        if node is None:
            return -1
        else:
            return node.height
    
    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left),
                      self.getHeight(node.right)) + 1

    def getMin(self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur

    def getMax(self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur

    def printAVL(self, node):
        if not node:
            return
        else:
            print("Key: ") + node.data + ("Height: ") + node.height
            self.printAVL(node.left)
            self.printAVL(node.right)
             

class MinHeap(BSTree):
    def insert(self, data):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        cur.right = BSNode(data)
        while cur.right.data < cur.data:
            tmp = cur
            cur = cur.right
            cur.right = tmp
    
    def getMin(self):
        minElem = self.root.data
        cur = self.root
        while cur.right.right is not None: 
            cur = cur.right
        self.root = cur.right
        cur.right = None

        #TODO: Fix so that you are just switching values not nodes
        #Must fix node children as well
        cur = self.root
        while cur.left.data < cur.data or cur.right.data < cur.data:
            curMin = cur.left if cur.left.data < cur.right.data else cur.right
            tmp = cur.left if curMin == cur.left else cur.right
            if tmp == cur.left:
                cur.left = cur
            else:
                cur.right = cur
            cur = tmp

        return minElem




def visit(node):
    return node.data

def inOrderTraversal(node):
    if node:    
        inOrderTraversal(node.left)
        visit(node)
        inOrderTraversal(node.right)

def preOrderTraversal(node):
    if node:
        visit(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

def postOrderTraversal(node):
    if node:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        visit(node)


def DFS(root):
    if not root: 
        return
    root.visit()
    for n in root.neighbors:
        if not n.visited:
            DFS(n)

def BFS(root):
    q = Queue()
    root.visit()
    q.add(root)
    
    while not q.isEmpty():
        r = q.remove()
        r.visit()
        for n in r.neighbors:
            if not n.visited:
                q.add(n)

