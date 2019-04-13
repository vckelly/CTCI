from .ll import Node
from .ll import SLinkedList
from .ll import DLinkedList
import pytest
import copy 

llist = SLinkedList(head=Node(data=1))
llist.insert(data=2)
llist.insert(data=3)
llist.insert(data=4)
llist.insert(data=5)

def test_init_func_SLL():
    head_node = Node(data=1)
    new_list = SLinkedList(head_node)
    assert new_list.head.get_data() == 1
    assert new_list.get_size() == 1

def test_len_SLL():
    assert len(llist) == 5

def test_get_size_SLL():
    assert llist.get_size() == 5
    
def test_insert_func_SLL():
    test_list = copy.copy(llist)   
    test_list.insert(data=6)
    assert test_list.get_size() == 6
    assert test_list.search(1) == 6
    
'''def test_print_vals(capsys):
    str_res = "Index 1: 4\nIndex 2: 3\nIndex 3: 2\nIndex 4: 1\n"
    llist.print_vals() 
    captured = capsys.readouterr()
    assert captured.out == str_res'''
    
def test_append_to_tail_SLL():
    test_list = copy.copy(llist)   
    test_list.append_to_tail(6)
    assert test_list.return_val_at_index(test_list.get_size()) == 6
    
def test_return_val_at_index_SLL():
    assert llist.return_val_at_index(1) == 5
    assert llist.return_val_at_index(2) == 4
    assert llist.return_val_at_index(3) == 3
    assert llist.return_val_at_index(4) == 2
    assert llist.return_val_at_index(5) == 1
    
def test_invalid_return_at_index_SLL():
    with pytest.raises(ValueError):
        assert llist.return_val_at_index(0) 
        assert llist.return_val_at_index(8) 
    
def test_search_valid_SLL():
    assert llist.search(3) == 3
    
def test_search_invalid_SLL():
    #with pytest.raises(ValueError):
    assert not llist.search(8)
    
def test_delete_SLL():
    test_list = copy.copy(llist)   
    test_list.delete(5)
    assert test_list.get_size() == 4
    assert not test_list.search(5)
    
def test_invalid_delete_SLL():
    test_list = copy.copy(llist)   
    with pytest.raises(ValueError):
        assert not test_list.delete(8)
    
def test_delete_at_index_SLL():
    test_list = copy.copy(llist)   
    test_list.delete_at_index(1)
    assert not test_list.search(5)
    assert test_list.get_size() == 4

    
###Testing of Doubly Linked List###
new_head = Node(1)
dllist = DLinkedList(head=new_head)
dllist.insert(2)
dllist.insert(3)
dllist.insert(4)
dllist.insert(5)

def test_init_DLL():
    head = Node(1)
    tail = Node(2)
    new_dll = DLinkedList(head=head, tail=tail)
    assert new_dll.head.data == 1
    assert new_dll.tail.data == 2

def test_insert_DLL():
    test_list = copy.copy(dllist)
    test_list.insert(6)
    assert test_list.get_size() == 6
    assert test_list.search(6) == 1
    
def test_append_to_tail_DLL():
    test_list = copy.copy(dllist)
    test_list.append_to_tail(6)
    assert test_list.get_size() == 6
    assert test_list.search(6) == 6
    
def test_delete_DLL():
    test_list = copy.copy(dllist)
    test_list.delete(3)
    assert test_list.get_size() == 4
    assert not test_list.search(3)
    
def test_invalid_delete_DLL():
    test_list = copy.copy(dllist)
    with pytest.raises(ValueError):
        assert not test_list.delete(8)
        