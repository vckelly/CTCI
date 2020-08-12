from .trees import BSNode, AVLNode, Graph, GraphNode, Tree, BSTree, AVLTree, Queue, \
                   inOrderTraversal, preOrderTraversal, postOrderTraversal, visit,\
                   DFS, BFS
import math
# Given a directed graph, determine if there
# is a route between two nodes
def routeBetweenNodes(graph, n1, n2):
    if n1 == n2:
        return True

    for n in graph.getNodes():
        n.visited = False

    q = Queue(first=n1)

    curNode = None
    while not q.isEmpty():
        curNode = q.remove()
        curNode.visit()
        for node in curNode.getNeighbors():
            if not node.visited:
                if node == n2:
                    return True
                node.visit()
                q.add(node)
    return False

def createMinimalBST(nArray):
    return BSTree(root=_createMinimalBST(nArray, 0, len(nArray)-1))

def _createMinimalBST(nArray, start, end):
    if end < start:
        return None
    mid = math.floor((start + end) / 2)

    n = nArray[mid]
    n.left = _createMinimalBST(nArray, start, mid - 1)
    n.right = _createMinimalBST(nArray, mid + 1, end)
    return n


#Given a binary tree, return a list of lists where each
#list represents the nodes at each level of the binary tree

def listOfDepths(bTree):
    lists = []
    _listOfDepths(bTree.root, lists, 0)
    # for i, x in enumerate(lists):
    #     cur = [n.data for n in x]
    #     print(i, cur)  
    return lists

def _listOfDepths(root, lists, level):
    if not root: 
        return
    newList = None
    if len(lists) == level:
        newList = []
        lists.append(newList)
    else:
        newList = lists[level]
    
    newList.append(root)
    _listOfDepths(root.left, lists, level+1)
    _listOfDepths(root.right, lists, level+1)

#Given a root node of a BST, validate that it is a 
#valid BST

#TODO fix func
# def validateBST(node, lastInt):
#     if not node:
#         return True
    
#     if not validateBST(node.left, lastInt):
#         return False

#     lastInt = node.data
    
#     if lastInt and not validateBST(node.right, lastInt):
#         return False

#     return True

def validateBST(node):
    return _validateBST(node, None, None)

def _validateBST(node, min, max):
    if not node:
        return True

    if (min != None and node.data <= min) or (max != None and node.data > max):
        return False
    
    if (not _validateBST(node.left, min, node.data)) or \
        not _validateBST(node.right, node.data, max):
        return False
    
    return True

def successor(node):
    if not node: 
        return None

    if node.right:
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x
    
def leftMostChild(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def topologicalSort(inpGraph):
    #pick any node, perform DFS on it. That node is marked PARTIAL
    #check on any children nodes that none are listed as PARTIAL...
    #otherwise we have a cycle.
    #Continue DFS until we reach end of path. Add that node to build order. 
    #Return through call stack, adding nodes as their children are added to the build order.
    buildOrder = []
    for node in inpGraph.getNodes():
        if node.status is "BLANK":
            if not doDFS(node, buildOrder):
                return None
            #print(" ".join([i.data for i in buildOrder]))
    return buildOrder[::-1]

#Helper for topological sort
def doDFS(node, stack):
    if node.status is "PARTIAL":
        return False

    if node.status is "BLANK":
        node.status = "PARTIAL"
        children = node.children
        for n in children:
            if not doDFS(n, stack):
                return False
        node.status = "DONE"
        stack.append(node)
    return True

#Given two nodes, return the first common ancestor between them
def firstCommonAncestor(p, q):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = goUpBy(second, abs(delta))

    while first is not second and first and second: 
        first = first.parent
        second = second.parent
    
    if not first or not second:
        return None

    return first

#Helper for firstCommonAncestor
def goUpBy(node, delta):
    while delta > 0 and node:
        node = node.parent
        delta -=1
    return node

#Helper for firstCommonAncestor
def depth(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

#Similar to firstCommonAncestor, but without using
#links to parents
def commonAncestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestorHelper(root, p, q)

#Helper for commonAncestor
def ancestorHelper(root, p, q):
    if not root or root is p or root is q:
        return root

    pIsOnLeft = covers(root.left, p)
    qIsOnLeft = covers(root.left, q)

    if pIsOnLeft is not qIsOnLeft:
        return root

    childSide = root.left if pIsOnLeft else root.right
    return ancestorHelper(childSide, p, q)

def covers(root, p):
    if not root:
        return False
    if root is p:
        return True
    return covers(root.left, p) or covers(root.right, p)
