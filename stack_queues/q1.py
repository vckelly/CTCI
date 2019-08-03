from datetime import datetime

class QueueNode(object):
    
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.last_node = None

class Queue(object):

    def __init__(self, first=None):
        if first:
            t = QueueNode(first)
            self.first = t
            self.last = t
        else:
            self.first = None
            self.last = None
        
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

class Animal(object):
    def __init__(self, name, animalType):
        self.name = name
        self.type = animalType
        self.timeStamp = datetime.now()


class AnimalQueue(object):
    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()

    def addAnimal(self, animal):
        if animal.type == 'Dog':
            self.dogQueue.add(animal)
        else:
            self.catQueue.add(animal)

    def removeCat(self):
        return self.catQueue.remove()
    
    def removeDog(self):
        return self.dogQueue.remove()
    
    def removeOldest(self):
        dog = self.dogQueue.peek()
        cat = self.catQueue.peek()

        if dog.timeStamp < cat.timeStamp:
            return self.dogQueue.remove()
        else:
            return self.catQueue.remove()