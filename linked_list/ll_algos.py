from .ll import SLinkedList, DLinkedList, Node

def remove_dups(LList):
    new_list = SLinkedList()
    cur = LList.head
    while cur:
        if not new_list.search(cur.get_data()):
            new_list.insert(cur.get_data())
        cur = cur.get_next()
    
    return new_list
    
def kth_to_last(LList, index):
    return LList.return_val_at_index(LList.get_size() - (index-1))

def partition(LList, index):
    new_list = SLinkedList()
    cur = LList.head
    while cur:
        if cur.get_data() >= index:
            new_list.append_to_tail(cur.get_data())
            cur = cur.get_next()
        else:
            new_list.insert(cur.get_data())
            cur = cur.get_next()
    
    if not isinstance(new_list, SLinkedList):
        raise TypeError("Wrong type: {type}!".format(type=str(type(sum_res))))
        
    return new_list
    

def sum_lists(list1, list2):
    sum_res = SLinkedList()
    if len(list1) != len(list2):
        raise ValueError("Lists are not equal length")
    
    carry = 0
    for i in range(1, len(list1)+1):
        cur_val = list1.return_val_at_index(i) \
        + list2.return_val_at_index(i)
        
        if not isinstance(cur_val, int):
            raise ValueError("Addition went wrong!")
        
        if cur_val > 9 and i == 1:
            cur_val -=10
            sum_res.append_to_tail(cur_val)
            carry = 1
    
        elif cur_val + carry > 19:
            cur_val -= 20
            sum_res.append_to_tail(cur_val)
            carry = 2
        
        elif cur_val > 9:
            cur_val -=10
            sum_res.append_to_tail(cur_val + carry)
            carry = 1 
            
        else:
            sum_res.append_to_tail(cur_val + carry)
            carry = 0
    
    if not isinstance(sum_res, SLinkedList):
        raise TypeError("Wrong type: {type}!".format(type=str(type(sum_res))))
        
    if sum_res.get_size() != 3:
        raise ValueError("list error")
    
    return sum_res
        
def is_palindrome(list1):
    front = 1
    back = list1.get_size()
    for i in range(1, int(back/2 + 1)):
        if list1.return_val_at_index(front) \
        != list1.return_val_at_index(back):
            return False
        else:
            front += 1
            back -= 1
    
    return True
    
def intersection(list1, list2):
    #get length and tail of list1
    len_1 = list1.get_size()
    cur = list1.head
    for i in range(len_1):
        cur = cur.get_next()
    tail_1 = cur
    
    #get length and tail of list2
    len_2 = list2.get_size()
    current = list2.head
    for i in range(len_2):
        current = current.get_next()
    tail_2 = current
    
    #if tails are different (by reference) return False
    if tail_1 is not tail_2:
        return False
        
    #set pointers to head of lists
    cur1 = list1.head
    cur2 = list2.head
    
    #set the pointer for the longer of the two lists
    #at the start of the common nodes between both lists
    if len_1 > len_2:
        for i in range((len_1 - len_2) + 1):
            cur1 = cur1.get_next()
    else:
        for i in range((len_2 - len_1) + 1):
            cur2 = cur2.get_next()
    
    while cur1 != cur2:
        cur1 = cur1.get_next()
        cur2 = cur2.get_next()
        if cur1 == None or cur2 == None:
            break
    
    if not isinstance(cur1, Node):
        raise ValueError("Returning Non Node Object")
    
    return cur1
    
        
        
