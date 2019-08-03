from .stack import Stack, StackNode, StackOfStacks, myQueue
from .q1 import Queue, QueueNode, Animal, AnimalQueue
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
from datetime import datetime

stack1 = Stack(1)
for i in range(2, 11):
    stack1.push(i)


def test_stack_init():
    stack_test = Stack(1)
    assert stack_test.isEmpty() == False
    assert stack_test.peek() == 1
    
def test_stack_init_empty():
    stack_test = Stack()
    assert stack_test.isEmpty() == True
    assert stack_test.min == None
    assert stack_test.capacity == 100

def test_stack_pop():
    stack_test = copy.copy(stack1)
    assert stack_test.pop() == 10

def test_stack_push():
    stack_test = copy.copy(stack1)
    stack_test.push(11)
    assert stack_test.peek() == 11

def test_stack_push_empty():
    stack_test = Stack()
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

def test_stack_sort():
    stack1 = Stack()
    for i in range(1, 11):
        stack1.push(i)
    assert stack1.curElems == 10
    assert stack1.peek() == 10
    stack1.sort()
    for i in range(1, 11):
        assert stack1.pop() == i

    stack2 = Stack()
    stack2.push(4)
    stack2.push(2)
    stack2.push(3)
    stack2.push(1)
    stack2.push(5)
    stack2.sort()
    for i in range(1,6):
        assert stack2.pop() == i
        
SoS1 = StackOfStacks(1)
for i in range(2, 11):
    SoS1.push(i)

def test_SoS_pop():
    stack_test = copy.copy(SoS1)
    assert stack_test.curIdx == 3
    assert stack_test.stackArr[3].peek() == 10
    assert stack_test.pop() == 10
    assert stack_test.curIdx == 2

def test_SoS_push():
    SoS1 = StackOfStacks(1)
    for i in range(2, 11):
        SoS1.push(i)
    #stack_test = copy.copy(SoS1)
    stack_test = SoS1

    assert stack_test.curIdx == 3
    assert stack_test.stackArr[3].peek() == 10
    assert type(stack_test.stackArr[2]) is Stack
    stack_test.push(11)
    assert stack_test.peek() == 11
    assert stack_test.curIdx == 3
    stack_test.push(12)
    stack_test.push(13)
    assert stack_test.curIdx == 4

def test_SoS_peek():
    SoS1 = StackOfStacks(1)
    for i in range(2, 11):
        SoS1.push(i)
    stack_test = SoS1
    #stack_test = copy.copy(SoS1)
    assert stack_test.peek() == 10
    stack_test.push(11)
    assert stack_test.peek() == 11

def test_SoS_popAt():
    SoS1 = StackOfStacks(1)
    for i in range(2, 11):
        SoS1.push(i)
    stack_test = SoS1
    #stack_test = copy.copy(SoS1)
    assert stack_test.popAt(3) == 10
    assert stack_test.popAt(0) == 3
    assert stack_test.peek() == 9


queue1 = Queue(1)
myQueue = myQueue()
myQueue.add(1)
for i in range(2, 11):
    queue1.add(i)
    myQueue.add(i)


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

def test_myQueue_add_remove():
    queue_test = copy.copy(myQueue)
    queue_test.add(11)
    assert queue_test.peek() == 1
    assert queue_test.size() == 11
    for i in range(1, 12):
        assert queue_test.remove() == i


dog1 = Animal('Boxer', 'Dog')
dog2 = Animal('Wilma', 'Dog')
dog3 = Animal('Sydney', 'Dog')
cat1 = Animal('Scratches', 'Cat')
cat2 = Animal('Toby', 'Cat')
cat3 = Animal('Furr', 'Cat')

def test_animal_init():
    test_animal = copy.copy(dog1)
    assert test_animal.type == 'Dog'
    assert test_animal.name == 'Boxer'
    assert type(test_animal.timeStamp) == datetime

aq = AnimalQueue()
def test_animal_queue_init():   
    test_queue = copy.deepcopy(aq)
    assert test_queue.catQueue.isEmpty() 
    assert test_queue.dogQueue.isEmpty()

def test_add_animal():
    test_queue = copy.deepcopy(aq)
    test_dog = copy.copy(dog1)
    test_cat = copy.copy(cat1)

    test_queue.addAnimal(test_dog)
    test_queue.addAnimal(test_cat)

    assert test_queue.dogQueue.peek() == test_dog
    assert test_queue.catQueue.peek() == test_cat

def test_remove_animal():
    test_queue = copy.deepcopy(aq)
    #test_queue = AnimalQueue()
    test_dog = copy.copy(dog1)
    test_cat = copy.copy(cat1)

    test_queue.addAnimal(test_dog)
    test_queue.addAnimal(test_cat)

    assert test_queue.dogQueue.peek() == test_dog
    assert test_queue.catQueue.peek() == test_cat

    test_queue.removeCat()
    test_queue.removeDog()
    assert test_queue.dogQueue.isEmpty()
    assert test_queue.catQueue.isEmpty() 

def test_remove_oldest():
    test_queue = copy.deepcopy(aq)
    tdog1 = copy.copy(dog1)
    tdog2 = copy.copy(dog2)
    tdog3 = copy.copy(dog3)
    tcat1 = copy.copy(cat1)
    tcat2 = copy.copy(cat2)
    tcat3 = copy.copy(cat3)

    test_queue.addAnimal(tdog1)
    test_queue.addAnimal(tdog2)
    test_queue.addAnimal(tdog3)
    test_queue.addAnimal(tcat1)
    test_queue.addAnimal(tcat2)
    test_queue.addAnimal(tcat3)

    assert not test_queue.dogQueue.isEmpty()
    assert not test_queue.catQueue.isEmpty()

    assert test_queue.removeOldest() == tdog1