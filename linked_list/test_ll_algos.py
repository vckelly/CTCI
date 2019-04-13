from .ll import SLinkedList, DLinkedList, Node
from .ll_algos import remove_dups, kth_to_last, \
               partition, sum_lists, is_palindrome, \
               intersection
import pytest
import copy 

llist = SLinkedList(head=Node(data=1))
llist.insert(data=2)
llist.insert(data=3)
llist.insert(data=4)
llist.insert(data=5)

def test_remove_dups():
    test_list = copy.copy(llist)
    test_list.insert(5)
    test_list.insert(3)
    assert test_list.get_size() == 7
    test_list = remove_dups(test_list)
    assert test_list.get_size() == 5

def test_kth_to_last():
    test_list = copy.copy(llist)
    assert kth_to_last(test_list, 1) == 1
    assert kth_to_last(test_list, 5) == 5
    assert kth_to_last(test_list, 3) == 3

def test_partition():
    assert llist.get_size() == 5
    test_list = copy.copy(llist)
    for i in range(6, 11):
        test_list.insert(i)
    
    assert test_list.get_size() == 10
    test_list = partition(test_list, 5)
    for item in range(1, int((len(test_list) / 2) - 1)):
        for item2 in range(int((len(test_list) / 2) + 1), \
            len(test_list) + 1):
            
            assert test_list.return_val_at_index(item) \
            < test_list.return_val_at_index(item2)

def test_sum_lists():
    list1 = SLinkedList()

    for i in range(1, 4):
        list1.insert(i)
    list2 = SLinkedList()
    for i in range(7, 10):
        list2.insert(i)
        
    ### list 1 == (3, 2, 1) ###
    ### list 2 == (9, 8, 7) ###
    ### answer == 912 ###
    ### res list == (2, 1, 9) ###
    
    assert len(list1) == 3
    assert len(list2) == 3
    res = sum_lists(list1, list2)
    assert res.get_size() == 3
    
    assert res.return_val_at_index(1) == 2
    assert res.return_val_at_index(2) == 1
    assert res.return_val_at_index(3) == 9

def test_is_palindrome():
    test_list = SLinkedList()
    test_list.insert('A')
    test_list.insert('B')
    test_list.insert('C')
    
    test_list.append_to_tail('A')
    test_list.append_to_tail('B')
    test_list.append_to_tail('C')
    
    ### test_list == (CBAABC)
    
    assert is_palindrome(test_list)
    
    tl = SLinkedList()
    
    tl.insert('!')
    tl.insert('A')
    tl.insert('B')
    tl.insert('C')
    
    tl.append_to_tail('A')
    tl.append_to_tail('B')
    tl.append_to_tail('C')
    
    ### tl == (CBA!ABC)
    
    assert is_palindrome(tl)
    
def test_is_palindrome_invalid():
    test_list = SLinkedList()
    
    test_list.insert('A')
    test_list.insert('B')
    test_list.insert('C')
    
    test_list.insert('Z')
    test_list.insert('Y')
    test_list.insert('X')
    
    ### test_list == (XYZCBA)
    
    assert not is_palindrome(test_list)
'''
def test_intersection():
    longer = SLinkedList()
    for i in range(1, 5):
        longer.insert(i)
        
    #longer == (4, 3, 2, 1)
    
    shorter = SLinkedList()
    for i in range(1, 3):
        shorter.insert(i)
        
    #shorter == (2, 1)
    
    for i in range(5, 8):
        new_node = Node(data=i)
        assert isinstance(new_node, Node)
        assert new_node.get_data() == i
        longer.append_node_to_tail(new_node)
        shorter.append_node_to_tail(new_node)

    #longer == (4, 3, 2, 1, 5, 6, 7)
    #shorter == (2, 1, 5, 6, 7)
    #collision occurs at node with value 5
    
    assert isinstance(shorter, SLinkedList) 
    assert isinstance(longer, SLinkedList)

    coll = intersection(shorter, longer)
    assert isinstance(coll, Node)
    assert longer.get_index_of_node(coll) == 5
    assert shorter.get_index_of_node(coll) == 3
'''
def test_intersection_invalid():
    list1 = SLinkedList()
    list2 = SLinkedList()
    for i in range(5):
        list1.insert(i)
        list2.insert(i)
    
    assert not intersection(list1, list2)
    
