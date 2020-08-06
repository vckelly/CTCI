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
    return BSTree(rNode=_createMinimalBST(nArray, 0, len(nArray)-1))

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