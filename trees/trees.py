import sys
sys.path.append('../stack_queues')
import Queue

class Node(object):
    def __init__(self, data=None):
        self.data = data if data else None
        self.children = []

class BSNode(object):
    def __init__(self, data=None):
        self.data = data if data else None
        self.left = self.right = None

class GraphNode(object):
    def __init__(self, data=None):
        self.data = data if data else None
        self.neighbors = []
        self.visited = False
    def visit(self)
        self.visited = True
        return self.data

class Tree(object):
    def __init__(self, data=None):
        self.root = Node(data)

class BSTree(object):
    def __init__(self, data=None):
        self.root = BSNode(data)

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
                queue.add(n)

