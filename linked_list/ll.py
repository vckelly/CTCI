
class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
        

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
    
    def get_prev(self):
        return self.prev_node
        

    def set_next(self, new_next):
        self.next_node = new_next
    
    def set_prev(self, new_prev):
        self.prev_node = new_prev   


class SLinkedList(object):

    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.size = 1
        else:
            self.size = 0
    
    def __len__(self):
        return self.size
    
    def set_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.get_next()

        return size
    
    def get_size(self):
        return self.size
        
    def print_vals(self):
        if self.get_size() < 1:
            print ("Empty LinkedList")
        else:
            current = self.head
            idx = 1
            while current:
                print ("Index " + str(idx) + ": " + str(current.get_data()) + "\n")
                idx += 1
                current = current.get_next()

    def insert(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            self.size += 1 
            return
        else:
            new_node.set_next(self.head)
            self.head = new_node
            self.size +=1
            
    def insert_node(self, new_node):
        if not self.head:
            self.head = new_node
            self.size += 1 
            return
        else:
            new_node.set_next(self.head)
            self.head = new_node
            self.size +=1
        
    def append_to_tail(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        cur = self.head
        while cur:
            if cur.get_next() == None:
                cur.set_next(new_node)
                self.size += 1
                return
            else:
                cur = cur.get_next()
    
    def append_node_to_tail(self, new_node):
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        cur = self.head
        while cur:
            if cur.get_next() == None:
                cur.set_next(new_node)
                self.size += 1
                return
            else:
                cur = cur.get_next()


    def search(self, data):
        current = self.head
        idx = 1
        while current:
            if current.get_data() == data:
                return idx
            else:
                current = current.get_next()
                idx += 1

        return False
    
    def is_node(self, node):
        if not self.head:
            return False
        cur = self.head
        while cur:
            if cur is node:
                return cur
            else:
                cur = cur.get_next()
        
        return False

    def delete(self, data):
        current = self.head
        last = None
        
        while current:
            if current.get_data() == data:
                if not last:
                    self.head = current.get_next()
                    self.size -= 1
                    return
                else:
                    last.set_next(current.get_next())
                    self.size -= 1
                    return
            else:
                last = current
                current = current.get_next()

        raise ValueError('Value not in list!')

    def delete_at_index(self, index):
        current = self.head

        if index < 1 or index > self.size:
            raise ValueError('Index not valid')
        else:
            for i in range(1, index):
                current = current.get_next()

            self.delete(current.get_data())
            
    def return_val_at_index(self, index):
        current = self.head
        if index < 1:
            raise ValueError("Enter indexes larger than 1")
            
        if index > self.size:
            raise ValueError("Enter index smaller than size of list")
            
        for i in range(1, index):
            current = current.get_next()
        
        return current.get_data()

    def get_index_of_val(self, data):
        if not self.head:
            return False
        idx = 1
        cur = self.head
        while cur:
            if cur.get_data() == data:
                return idx
            else:
                cur = cur.get_next()
                idx +=1
        
        return False
    
    def get_index_of_node(self, node):
        if not self.head:
            return False
        idx = 1
        cur = self.head
        while cur:
            if cur is node:
                return idx
            else:
                cur = cur.get_next()
                idx +=1
        
        return False

class DLinkedList(SLinkedList):
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        if self.head and not self.tail:
            self.tail = self.head
        self.size = self.set_size()
        
    def insert(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = self.tail = new_node
            self.size += 1 
            return
            
        new_node.set_next(self.head)
        self.head.set_prev(new_node)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1
        
    def append_to_tail(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = self.tail = new_node
            self.size += 1
            return
        self.tail.set_next(new_node)
        new_node.set_prev(self.tail)
        self.tail = new_node
        self.size += 1
    
    def delete(self, data):
        current = self.head
        last = None

        while current:
            if current.get_data() == data:
                if current == self.tail:
                    last.set_next(None)
                    self.tail = last
                    self.size -= 1
                    return
                else:
                    last.set_next(current.get_next())
                    self.size -= 1
                    return
            else:
                last = current
                current = current.get_next()

        raise ValueError('Value not in list!')
    
    