from .ll import SLinkedList, DLinkedList

def remove_dups(LList):
    new_list = SLinkedList()
    cur = LList.head
    while cur:
        if not new_list.search(cur.get_data()):
            new_list.insert(cur.get_data())
        cur = cur.get_next()
    
    return new_list
    
def kth_to_last(LList, index):
    return LList.return_val_at_index(LList.size() - index)
    

    