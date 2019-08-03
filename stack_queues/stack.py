class StackNode(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        #self.last_node = None
        self.stack_min = None

class Stack(object):

    def __init__(self, top=None, capacity=None):
        if top: 
            t = StackNode(data=top)
            self.top = t
            self.min = t.data
            self.curElems = 1
        else: 
            self.top = None
            self.min = None
            self.curElems = 0
        
        self.capacity = capacity or 100
        
        
        
    def pop(self):
        if self.top is None:
            raise ValueError("Error: Empty stack!")
        
        if self.top.data == self.min:
            if self.top.next_node is not None:
                self.min = self.top.next_node.stack_min
            else:
                self.min = None
        res = self.top.data
        self.top = self.top.next_node
        self.curElems-=1
        return res

    def push(self, item):
        t = StackNode(data=item)
        if not self.min or self.min > item:
            self.min = item
        t.next_node = self.top
        t.stack_min = self.min
        self.top = t
        self.curElems+=1

    def peek(self):
        if self.top is None:
            raise ValueError('Stack is empty!')
        return self.top.data
        

    def isEmpty(self):
        return self.top is None
    
    def getMin(self):
        if self.isEmpty():
            raise ValueError("Stack is empty!")
        return self.min
    
    def sort(self):
        r = Stack()
        while not self.isEmpty():
            tmp = self.pop()
            while not r.isEmpty() and r.peek() > tmp:
                self.push(r.pop())
            r.push(tmp)
        while not r.isEmpty():
            self.push(r.pop())

        


        
class StackOfStacks(object):
    
    def __init__(self, top=None):
        self.stackArr = []
        first = Stack(top=top, capacity=3)
        self.stackArr.append(first)
        self.curIdx = 0

    def push(self, item):
        if self.stackArr[self.curIdx].curElems >= self.stackArr[self.curIdx].capacity:
            newStack = Stack(top=item, capacity=3)
            self.curIdx+=1
            self.stackArr.append(newStack)
            
        else:
            self.stackArr[self.curIdx].push(item)
        
    def pop(self):
        if self.stackArr[self.curIdx].curElems > 1:
            return self.stackArr[self.curIdx].pop()
            
        else:
            res = self.stackArr[self.curIdx].pop()
            self.stackArr[self.curIdx] = None
            self.curIdx-=1
            return res
    
    def peek(self):
        if self.stackArr[0] is None:
            raise ValueError('Stack is empty!')
        return self.stackArr[self.curIdx].peek()

    def popAt(self, index):
        if self.curIdx < index: 
            raise ValueError('There is no stack at the provided index!')
        elif index == self.curIdx: 
            return self.pop()
        else: 
            return self.stackArr[index].pop()

class myQueue(object):
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack()

    def size(self):
        return self.stackNewest.curElems + self.stackOldest.curElems
    
    #adds new item onto stackNewest
    def add(self, item):
        self.stackNewest.push(item)

    def shiftStacks(self):
        if self.stackOldest.isEmpty():
            while not self.stackNewest.isEmpty():
                self.stackOldest.push(self.stackNewest.pop())

    def peek(self):
        self.shiftStacks() #ensure stackOldest has the current elements
        return self.stackOldest.peek()
    
    def remove(self):
        self.shiftStacks()
        return self.stackOldest.pop()