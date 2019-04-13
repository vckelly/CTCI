class StackNode(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        #self.last_node = None
        self.stack_min = None

class Stack(object):

    def __init__(self, top=None, capacity=None):
        t = StackNode(data=top)
        self.top = t
        self.min = t.data
        self.capacity = capacity
        self.curElems = 1
        
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
        if self.min > item:
            self.min = item
        t.next_node = self.top
        t.stack_min = self.top.stack_min
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
        
class StackOfStacks(object):
    
    def __init__(self, top=None):
        self.stackArr = []
        first = Stack(top=top, capacity=3)
        self.stackArr.append(first)
        self.curIdx = 0

    def push(self, item):
        if self.stackArr[self.curIdx].curElems >= self.stackArr[self.curIdx].capacity:
            new = Stack(top=item, capacity=3)
            self.curIdx+=1
            self.stackArr.append(new)
            
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
        

