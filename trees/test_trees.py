
from .trees import Node, BSNode, AVLNode, GraphNode, Graph, Tree, \
                   BSTree, AVLTree, MinHeap    
from .tree_algs import routeBetweenNodes, createMinimalBST, listOfDepths, validateBST, \
                       successor, topologicalSort, firstCommonAncestor
 
import pytest
import copy 
import string
import timeit
from datetime import datetime

BSTNodes = []
for i in range(10):
    n = BSNode(data=i)
    BSTNodes.append(n)

avl = AVLTree(data=0)
for i in range(1, 10):
    avl.root.insert(AVLNode(data=i))

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
gNodes = []
for idx, item in enumerate(nodes):
    n = GraphNode(item)
    gNodes.append(n)

assert isinstance(gNodes[0], GraphNode) 
#A
gNodes[0].addNeighbor(neighbor=gNodes[1])
#B
gNodes[1].addNeighbor(nList=[gNodes[0], gNodes[2]])
#C
gNodes[2].addNeighbor(nList=[gNodes[1], gNodes[3]])
#D
gNodes[3].addNeighbor(nList=[gNodes[2], gNodes[4]])
#E
gNodes[4].addNeighbor(neighbor=gNodes[3])
#F
gNodes[5].addNeighbor(neighbor=gNodes[4])
#G
gNodes[6].addNeighbor(neighbor=gNodes[4])

assert gNodes[1] in gNodes[0].getNeighbors()
assert gNodes[2] in gNodes[1].getNeighbors() 
g = Graph(gNodes)
assert isinstance(g, Graph)
for node in gNodes:
    assert node in g.getNodes()
    
def test_routeBetweenNodes():
    gt = copy.copy(g)
    assert routeBetweenNodes(gt, gNodes[4], gNodes[1])
    assert routeBetweenNodes(gt, gNodes[1], gNodes[3])
    assert routeBetweenNodes(gt, gNodes[6], gNodes[2])
    assert not routeBetweenNodes(gt, gNodes[2], gNodes[6])
    assert not routeBetweenNodes(gt, gNodes[0], gNodes[5])
    assert not routeBetweenNodes(gt, gNodes[6], gNodes[5])

def test_minimalBST():
    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    assert isinstance(myT, BSTree)
    assert isinstance(myT.root, BSNode)
    assert myT.root.data == 4
    assert myT.getHeight(myT.root) == 3

def test_BST_Print():
    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    #myT.printTree(myT.root)
    #assert False

def test_listOfDepths():
    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    lists = listOfDepths(myT)
    for i in range(len(lists)):
        lists[i] = [n.data for n in lists[i]]
    assert lists[0] == [4]
    assert lists[1] == [1, 7]
    assert lists[2] == [0, 2, 5, 8]
    assert lists[3] == [3, 6, 9]
    
def test_isBalanced():
    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)

    unbalanced = []
    for i in range(5):
        n = BSNode(data=i)
        unbalanced.append(n)
        if i != 0:
            unbalanced[i-1].right = n

    unbalancedT = BSTree(root=unbalanced[0])
    
    assert myT.isBalanced(myT.root)
    assert not unbalancedT.isBalanced(unbalancedT.root)
    
    unbalanced = []
    for i in range(5):
        n = BSNode(data=i)
        unbalanced.append(n)
        if i > 1:
            unbalanced[i-1].right = n
        else:
            unbalanced[i-1].left = n
        
    unbalancedT = BSTree(root=unbalanced[0])
    assert not unbalancedT.isBalanced(unbalancedT.root)

def test_vaildateBST():
    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    assert validateBST(myT.root)

    notValid = []
    for i in range(5):
        n = BSNode(data=i)
        notValid.append(n)
        if i > 0:
            if i % 2 == 0:
                notValid[i-1].left = n
            else:
                notValid[i-1].right = n
    assert isinstance(notValid[4], BSNode)
    assert notValid[3].left == notValid[4]
    myT = BSTree(root=notValid[0])        
    assert not validateBST(myT.root)

def test_successor():
    myAvl = copy.copy(avl)
    assert isinstance(myAvl, AVLTree)
    assert myAvl.root.right.data == 1
    assert successor(myAvl.root).data == 1

    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    assert successor(myT.root).data == 5

nodes = []
for ch in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    n = Node(data=ch)
    nodes.append(n)
#A
nodes[0].parent = [nodes[5], nodes[2], nodes[1]]
nodes[0].children = [nodes[4]]
#B
nodes[1].parent = [nodes[5]]
nodes[1].children = [nodes[4], nodes[0], nodes[7]]
#C
nodes[2].parent = [nodes[5]]
nodes[2].children = [nodes[0]]
#D
nodes[3].parent = []
nodes[3].children = [nodes[6]]
#E
nodes[4].parent = [nodes[0], nodes[1]]
nodes[4].children = []
#F
nodes[5].parent = []
nodes[5].children = [nodes[2], nodes[1], nodes[0]]
#G
nodes[6].parent = [nodes[3]]
nodes[6].children = []
#H
nodes[7].parent = [nodes[1]]
nodes[7].children = []

def test_topoSort():
    n = copy.copy(nodes)
    g = Graph(nodes=n)
    res = topologicalSort(g)
    #print(" ".join(i.data for i in res))
    strs = [i.data for i in res]
    assert strs.index("E") > strs.index("A")
    assert strs.index("G") > strs.index("D")
    assert strs.index("A") > strs.index("C")
    assert strs.index("F") < strs.index("B")

def test_firstCommonAncestor():
    n = copy.copy(BSTNodes)
    myT = createMinimalBST(n)
    myT.addParents(myT.root)

    assert firstCommonAncestor(myT.root.left.left, myT.root.left.right) \
        is myT.root.left

    assert firstCommonAncestor(myT.root.left.left, myT.root.right.right) \
    is myT.root