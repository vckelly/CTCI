from .stack import Stack, StackNode, StackOfStacks
from .queue import Queue, QueueNode
# from .string_algs import is_unique_ascii, naive_is_unique_ascii,\
#                   is_permutation, naive_is_permutation,\
#                   naive_URLify, URLify,\
#                   is_palindrome_permutation,\
#                   one_away, \
#                   string_compression, \
#                   zero_matrix, \
#                   rotate_matrix
               
import pytest
import copy 
import string
import timeit

stack1 = Stack(1)
for i in range(2, 11):
    stack1.push(i)


def test_stack_init():
    stack_test = Stack(1)
    assert stack_test.isEmpty() == False
    assert stack_test.peek() == 1
    

def test_stack_pop():
    stack_test = copy.copy(stack1)
    assert stack_test.pop() == 10

def test_stack_push():
    stack_test = copy.copy(stack1)
    stack_test.push(11)
    assert stack_test.peek() == 11

def test_stack_peek():
    stack_test = copy.copy(stack1)
    assert stack_test.peek() == 10
    
def test_stack_min():
    stack_test = copy.copy(stack1)
    assert stack_test.getMin() == 1
    
    stack2 = Stack(10)
    for i in range(10,0,-1):
        stack2.push(i)
    
    for j in range(11):
        assert stack2.getMin() == i
        
SoS1 = StackOfStacks(1)
for i in range(2, 11):
    SoS1.push(i)

def test_SoS_pop():
    stack_test = copy.copy(SoS1)
    assert stack_test.curIdx == 3
    assert stack_test.pop() == 10
    assert stack_test.curIdx == 2

def test_SoS_push():
    stack_test = copy.copy(SoS1)
    stack_test.push(11)
    assert stack_test.peek() == 11
    assert stack_test.curIdx == 3
    stack_test.push(12)
    stack_test.push(13)
    assert stack_test.curIdx == 4
    
queue1 = Queue(1)
for i in range(2, 11):
    queue1.add(i)
    
def test_queue_init():
    queue_test = Queue(1)
    assert queue_test.first.data == 1
    assert queue_test.last.data == 1
    assert queue_test.isEmpty() == False
    
def test_queue_add():
    queue_test = copy.copy(queue1)
    queue_test.add(11)
    assert queue_test.first.data == 1
    assert queue_test.last.data == 11

def test_queue_remove():
    queue_test = copy.copy(queue1)
    queue_test.remove()
    assert queue_test.first.data == 2
    assert queue_test.last.data == 10
    for i in range(2, 10):
        queue_test.remove()
        assert queue_test.first.data == i+1
    assert queue_test.first.data == 10
    assert queue_test.last.data == 10