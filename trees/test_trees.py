
from .trees import Node, BSNode, AVLNode, GraphNode, Graph, Tree, \
                   BSTree, AVLTree, MinHeap    
from .tree_algs import routeBetweenNodes, createMinimalBST, listOfDepths, validateBST, \
                       successor
 
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
    myT.printTree(myT.root)
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

    unbalancedT = BSTree(rNode=unbalanced[0])
    
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
        
    unbalancedT = BSTree(rNode=unbalanced[0])
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
    myT = BSTree(rNode=notValid[0])        
    assert not validateBST(myT.root)

def test_successor():
    myAvl = copy.copy(avl)
    assert isinstance(myAvl, AVLTree)
    assert myAvl.root.right.data == 1
    assert successor(myAvl.root).data == 1

    nodes = copy.copy(BSTNodes)
    myT = createMinimalBST(nodes)
    assert successor(myT.root).data == 5

# def test_stack_init():
#     stack_test = Stack(1)
#     assert stack_test.isEmpty() == False
#     assert stack_test.peek() == 1
    
# def test_stack_init_empty():
#     stack_test = Stack()
#     assert stack_test.isEmpty() == True
#     assert stack_test.min == None
#     assert stack_test.capacity == 100

# def test_stack_pop():
#     stack_test = copy.copy(stack1)
#     assert stack_test.pop() == 10

# def test_stack_push():
#     stack_test = copy.copy(stack1)
#     stack_test.push(11)
#     assert stack_test.peek() == 11

# def test_stack_push_empty():
#     stack_test = Stack()
#     stack_test.push(11)
#     assert stack_test.peek() == 11

# def test_stack_peek():
#     stack_test = copy.copy(stack1)
#     assert stack_test.peek() == 10
    
# def test_stack_min():
#     stack_test = copy.copy(stack1)
#     assert stack_test.getMin() == 1
    
#     stack2 = Stack(10)
#     for i in range(10,0,-1):
#         stack2.push(i)
    
#     for j in range(11):
#         assert stack2.getMin() == i

# def test_stack_sort():
#     stack1 = Stack()
#     for i in range(1, 11):
#         stack1.push(i)
#     assert stack1.curElems == 10
#     assert stack1.peek() == 10
#     stack1.sort()
#     for i in range(1, 11):
#         assert stack1.pop() == i

#     stack2 = Stack()
#     stack2.push(4)
#     stack2.push(2)
#     stack2.push(3)
#     stack2.push(1)
#     stack2.push(5)
#     stack2.sort()
#     for i in range(1,6):
#         assert stack2.pop() == i
        
# SoS1 = StackOfStacks(1)
# for i in range(2, 11):
#     SoS1.push(i)

# def test_SoS_pop():
#     stack_test = copy.copy(SoS1)
#     assert stack_test.curIdx == 3
#     assert stack_test.stackArr[3].peek() == 10
#     assert stack_test.pop() == 10
#     assert stack_test.curIdx == 2

# def test_SoS_push():
#     SoS1 = StackOfStacks(1)
#     for i in range(2, 11):
#         SoS1.push(i)
#     #stack_test = copy.copy(SoS1)
#     stack_test = SoS1

#     assert stack_test.curIdx == 3
#     assert stack_test.stackArr[3].peek() == 10
#     assert type(stack_test.stackArr[2]) is Stack
#     stack_test.push(11)
#     assert stack_test.peek() == 11
#     assert stack_test.curIdx == 3
#     stack_test.push(12)
#     stack_test.push(13)
#     assert stack_test.curIdx == 4

# def test_SoS_peek():
#     SoS1 = StackOfStacks(1)
#     for i in range(2, 11):
#         SoS1.push(i)
#     stack_test = SoS1
#     #stack_test = copy.copy(SoS1)
#     assert stack_test.peek() == 10
#     stack_test.push(11)
#     assert stack_test.peek() == 11

# def test_SoS_popAt():
#     SoS1 = StackOfStacks(1)
#     for i in range(2, 11):
#         SoS1.push(i)
#     stack_test = SoS1
#     #stack_test = copy.copy(SoS1)
#     assert stack_test.popAt(3) == 10
#     assert stack_test.popAt(0) == 3
#     assert stack_test.peek() == 9


# queue1 = Queue(1)
# myQueue = myQueue()
# myQueue.add(1)
# for i in range(2, 11):
#     queue1.add(i)
#     myQueue.add(i)


# def test_queue_init():
#     queue_test = Queue(1)
#     assert queue_test.first.data == 1
#     assert queue_test.last.data == 1
#     assert queue_test.isEmpty() == False
    
# def test_queue_add():
#     queue_test = copy.copy(queue1)
#     queue_test.add(11)
#     assert queue_test.first.data == 1
#     assert queue_test.last.data == 11

# def test_queue_remove():
#     queue_test = copy.copy(queue1)
#     queue_test.remove()
#     assert queue_test.first.data == 2
#     assert queue_test.last.data == 10
#     for i in range(2, 10):
#         queue_test.remove()
#         assert queue_test.first.data == i+1
#     assert queue_test.first.data == 10
#     assert queue_test.last.data == 10

# def test_myQueue_add_remove():
#     queue_test = copy.copy(myQueue)
#     queue_test.add(11)
#     assert queue_test.peek() == 1
#     assert queue_test.size() == 11
#     for i in range(1, 12):
#         assert queue_test.remove() == i
