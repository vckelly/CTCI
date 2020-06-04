#!/usr/bin/env python

import time
from collections import Counter

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


class HashTable(object):
    
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.data = [[] for i in range(capacity)]
    
    def get_size(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def get_data(self):
        return self.data
        
    def hash_function(self, key_str, size):
        return sum([ord(c) for c in key_str]) % size
        
            
    def insert(self, key, val):
        key_hash = self.hash_function(key, self.capacity)
        key_value = [key, val]
        #check if key alrady exists
        #if so, then update and return
        for pair in self.data[key_hash]:
            if key == pair[0]:
                pair[1] = val
                if self.get(key) == val:
                    return True
                else:
                    return False
                
        #key is not in hash table, add key/val pair
        self.size += 1
        self.data[key_hash].append(key_value)
        if self.get(key) == val:
            return True
        else:
            return False
            
    def get(self, key):
        key_hash = self.hash_function(key, self.capacity)
        if len(self.data[key_hash]) < 1:
            return False
        else:
            for pair in self.data[key_hash]:
                if pair[0] == key:
                    return pair[1]
                    
        return False
    
    def delete(self, key):
        key_hash = self.hash_function(key, self.capacity)
        if len(self.data[key_hash]) < 1:
            return False
            
        for index in range(len(self.data[key_hash])):
            if self.data[key_hash][index][0] == key:
                self.data[key_hash].pop(index)
                self.size -= 1
                return True
    
    def print_table(self):
        res = []
        res.append("Hash Table Contents\n")
        for item in self.data:
            if item is not None:
                res.append(str(item))
        
        return ''.join(res) 

def naive_is_unique_ascii(str_input, duration=.000001):
    #assume ascii string input
    time0 = time.time()
    if len(str_input) == 1:
        return True
    
    bool_dict = {}
    for ch in str_input:
        if ch not in bool_dict.keys():
            bool_dict[ch] = True
        else:
            time1 = time.time()
            print (time1 - time0)
            return False
    time2 = time.time()
    print (time2 - time0)
    return True

def is_unique_ascii(str_input):
    #assume ascii string input
    if len(str_input) > 128:
        return False
    
    if len(str_input) == 1:
        return True
    
    char_set = [False for _ in range(128)]
    for char in str_input:
        val = ord(char)
        if char_set[val]:
            #char already found
            return False
        char_set[val] = True
        
    return True
    
def naive_is_permutation(string1, string2):
    list1 = sorted([i for i in string1])
    list2 = sorted([j for j in string2])
    if list1 == list2:
        return True
    return False

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    count = Counter()
    for char in string1:
        count[char] += 1
    
    for ch in string2:
        if count[ch] <= 0:
            return False
        count[ch] -= 1
    
    return True

def URLify(string1, length):
    #CTCI example uses string index assignment, not possible in Python
    new_index = len(string1)
    res_str = [char for char in string1]
    for i in reversed(range(length)):
        if string1[i] == ' ':
            res_str[i] = '%20'

    return "".join(res_str)


def naive_URLify(string1, length):
    replace_str ="%20"
    string1 = string1.rstrip()
    res = []
    for i in range(length):
        if string1[i] == " ":
           res.append(replace_str)
        else:
            res.append(str(string1[i]))
           
    return ''.join(res)

def reverse_string(string1):
    if len(string1) == 1:
        return string1

    out = [None for i in range(len(string1))]

    ptr1 = 0
    ptr2 = len(string1)-1

    while ptr2 >= ptr1:
        out[ptr1] = string1[ptr2] 
        out[ptr2] = string1[ptr1]
        ptr1 += 1
        ptr2 -= 1

    return "".join(out)

def reverse_string_noArr(string1):
    if len(string1) == 1:
        return string1

    out = ""

    ptr1 = 0
    ptr2 = len(string1)-1

    while ptr2 >= ptr1:
        if ptr1 > 0:
            firstHalf = out[:ptr1]
            firstHalf = firstHalf + string1[ptr2]
            secondHalf = out[ptr1:]
            secondHalf = string1[ptr2] + secondHalf 
            out = firstHalf + secondHalf
        else:
            out = string1[ptr2] + string1[ptr1]
        ptr1 += 1
        ptr2 -= 1

    return out

def is_palindrome_permutation(string1):
    
    #1. If string is only one character, return True
    #2. Strip all whitespace from string
    #3. Determine length of string
    #4. If even, each character should appear an even number of times
    #5. If odd, one character should appear an odd number of times. 
    #6. All other characters should appear an even number of times
    
    if len(string1) == 1:
        return True
        
    string1 = string1.strip()
    len_string = len(string1)
    hash_t = HashTable()
    for i in range(len_string):
        hash_t.insert(string1[i], string1.count(string1[i]))
    
    if len_string % 2 == 0:
        for item in hash_t.get_data():
            for item2 in item:
                if item2[1] % 2 != 0:
                    return False
    
        return True
    
    else:
        odd_count = False
        for item in hash_t.get_data():
            for item2 in item:
                if item2[1] % 2 != 0 and not odd_count:
                    odd_count = True
                
                elif item2[1] % 2 != 0:
                    return False
                
        return True 
                
    raise ValueError("Something went wrong!")
            
def one_away(string1, string2):
   
    string1 = string1.strip()
    string2 = string2.strip()
    if string1 == string2:
        return True
    
    hash1 = HashTable()
    for item in range(len(string1)):
         assert hash1.insert(string1[item], string1.count(string1[item]))
    
    hash2 = HashTable()
    for item2 in range(len(string2)):
        assert hash2.insert(string2[item2], string2.count(string2[item2]))
    
    one_off = False
    
    for hash_idx in hash1.get_data():
        for i in range(len(hash_idx)):
            #if same characters in each string are off by 1
            #and no other character pairs have been identified as
            #being "one off", switch boolean to indicate such a pair
            #has been found
            if abs(hash1.get(hash_idx[i][0]) - hash2.get(hash_idx[i][0])) == 1 \
            and not one_off:
                one_off = True
            
            #if there is a "one off" pair identified and it is not the first
            #such pair to be found, return False
            elif abs(hash1.get(hash_idx[i][0]) - hash2.get(hash_idx[i][0])) > 0 \
            and one_off:
                return False
            
    return True
    
def string_compression(string1):

    string1 = string1.strip()

    original = string1 

    result_list = []
    end_list = False
    index = 0
    
    #while not end_list:
    while index < len(string1):
        count = 1
        if index != len(string1) - 1 and string1[index] != string1[index+1]:
            result_list.append((string1[index], count))
            
        else:
            for j in range(index+1, len(string1)):
                if string1[index] == string1[j]:
                    count += 1
                else:
                    break
            result_list.append((string1[index], count))
            
        index += count
        
        #if index >= len(string1):
            #end_list = True
            
    str_res = []     
    for pair in result_list:
        str_res.append(str(pair[0]))
        str_res.append(str(pair[1]))
    
    str_res = ''.join(str_res)
    if len(str_res) >= len(original):
        return original
    else:
        return str_res

def zero_matrix(matrix):
    
    row_len = len(matrix)
    columns = len(matrix[0])
    zero_rows = []
    zero_cols = []
    
    for master_idx in range(row_len):
        if 0 not in matrix[master_idx]:
            continue
        else:
            for idx in range(len(matrix[master_idx])):
                if matrix[master_idx][idx] == 0:
                    zero_cols.append(idx)
                    zero_rows.append(master_idx)
            
    for row in zero_rows:
        matrix[row] = [0 for i in range(row_len)]
    
    for cols in zero_cols:
        for i in range(row_len):
            matrix[i][cols] = 0
        
    return matrix
        
def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    
    n = len(matrix)
    layer = 0
    while(layer < n / 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            #save top
            top = matrix[first][i]
            
            #left -> top
            matrix[first][i] = matrix[last-offset][first]
            
            #bottom -> left
            matrix[last-offset][i] = matrix[last][last-offset]
            
            #right -> bottom
            matrix[last][last-offset] = matrix[i][last]
            
            #top -> right
            matrix[i][last] = top
        
        layer+=1
            
    for i in range(len(matrix)):                
        print(matrix[i])
        
    
def main():
    myStr = "hello"
    print("Reversed str is " + reverse_string(myStr))
    print("Reversed str is " + reverse_string_noArr(myStr))


if __name__ == "__main__":
    main()