class QueueNode(object):
    
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.last_node = None

class Queue(object):

    def __init__(self, first=None):
        t = QueueNode(first)
        self.first = t
        self.last = t
        
    def remove(self):
        if self.first is None:
            raise ValueError('Queue is empty!')
        data = self.first.data
        self.first = self.first.next_node
        
        if self.first is None:
            self.last = None
            
        return data

    def add(self, item):
        t = QueueNode(data=item)
        if self.last is not None:
            self.last.next_node = t
            
        self.last = t
        
        if self.first is None:
            self.first = self.last

    def peek(self):
        if self.first is None:
            raise ValueError('Queue is empty!')
        
        return self.first.data
        

    def isEmpty(self):
        return self.first is None
    