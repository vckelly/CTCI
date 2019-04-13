from .string_algs import HashTable, Node
from .string_algs import is_unique_ascii, naive_is_unique_ascii,\
                  is_permutation, naive_is_permutation,\
                  naive_URLify, URLify,\
                  is_palindrome_permutation,\
                  one_away, \
                  string_compression, \
                  zero_matrix, \
                  rotate_matrix
               
import pytest
import copy 
import string
import timeit

hash1 = HashTable()
letters = [letter for letter in string.ascii_lowercase]
for idx, letter in enumerate(letters):
    hash1.insert(letter, idx)

def test_hash_init():
    hash_test = HashTable()
    assert hash_test.get_size() == 0
    assert hash_test.get_capacity() == 1000
    assert len(hash_test.get_data()) == 1000

def test_hash_insert_get():
    hash_test = copy.copy(hash1)
    
    for index, l in enumerate(letters):
        assert hash_test.get(l) == index
    
    assert hash_test.get_size() == len(string.ascii_lowercase)

def test_hash_delete():
    hash_test = copy.copy(hash1)
    hash_test.delete('z')
    hash_test.delete('a')
    hash_test.delete('b')
    for letters in ['z', 'a', 'b']:
        assert not hash_test.get(letters)
    
    assert hash_test.get_size() == \
    len(string.ascii_uppercase) - 3
    
def test_hash_delete_invalid():
    hash_test = copy.copy(hash1)
    assert not hash_test.delete("A")

def test_print_table():
    hash_test = copy.copy(hash1)
    result = "Hash Table Contents\n"
    for list in hash_test.get_data():
        result += str(list)
    
    assert result == hash_test.print_table()
    
def test_is_unique():
    str_input = 'uniq'
    assert is_unique_ascii(str_input)
    assert is_unique_ascii(string.ascii_lowercase)
    assert not is_unique_ascii('unique')


def test_naive_is_unique():
    str_input = 'uniq'
    assert naive_is_unique_ascii(str_input)
    assert naive_is_unique_ascii(string.ascii_lowercase)
    assert not naive_is_unique_ascii('unique')
    
def test_is_permutation():
    assert is_permutation("abc", "cba")
    assert is_permutation("HelLo", "HLleo")
    assert not is_permutation("nope", "nopE")
    assert not is_permutation(string.ascii_uppercase, string.ascii_lowercase)
    assert is_permutation('12345', '54321')
    assert not is_permutation('12345', '67890')
    
def test_naive_is_permutation():
    assert naive_is_permutation("abc", "cba")
    assert naive_is_permutation("HelLo", "HLleo")
    assert not naive_is_permutation("nope", "nopE")
    assert not naive_is_permutation(string.ascii_uppercase, string.ascii_lowercase)
        
def test_URLify():
    replace_str = "%20"
    
    inp = "H e l l o"
    res = inp.replace(' ', replace_str)
    test = URLify(inp, len(inp))
    assert test == res

def test_naive_URLify():
    replace_str = "%20"
    
    inp = "H e l l o"
    res = inp.replace(' ', replace_str)
    test = naive_URLify(inp, len(inp))
    assert test == res
    
def test_palindrome_permutation():
    str1 = 'racecar'
    str2 = 'eacarcr'
    str3 = 'notpalindrome'
    str4 = 'abcabc'
    str5 = 'a'
    str6 = 'aaaaaa'
    str7 = 'aabbbbcccaabbbb'
    
    assert is_palindrome_permutation(str1)
    assert is_palindrome_permutation(str2)
    assert not is_palindrome_permutation(str3)
    assert is_palindrome_permutation(str4)
    assert is_palindrome_permutation(str5)
    assert is_palindrome_permutation(str6)
    assert is_palindrome_permutation(str7)


def test_one_away():
    str1 = 'hello'
    str2 = 'hell'
    assert one_away(str1, str2)
    
    str3 = 'whatthe'
    str4 = 'whate'
    assert not one_away(str3, str4)
    
    str5 = 'h'
    str6 = 'e'
    assert one_away(str5, str6)
    
    str7 = 'verylongone'
    str8 = 'verylongonee'
    assert one_away(str7, str8)
    
    assert one_away('a', 'a')
    assert one_away('backwards', 'sdrawkcab')
    assert one_away('evennn', 'evennil')
    assert one_away('evennn', 'evennil')
    assert one_away('evennn', 'oddnot')
    
def test_string_compression():
    string1 = 'aabcccccaaa'
    assert string_compression(string1) \
    == 'a2b1c5a3'
    
    string2 = 'zzyyyeeRRRq'
    assert string_compression(string2) \
    == 'z2y3e2R3q1'
    
    string3 = 'abc'
    assert string_compression(string3) \
    == string3
    
def test_matrix_zero():
    matrix = [[1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 4, 3],
              [0, 1, 2, 3]]
              
    res = [[0, 2, 3, 4],
           [0, 2, 3, 4],
           [0, 2, 4, 3],
           [0, 0, 0, 0]]
           
    assert zero_matrix(matrix) == res
    
    matrix2 = [[1, 2, 3, 4],
              [1, 2, 0, 4],
              [1, 2, 4, 3],
              [0, 1, 2, 0]]
              
    res2 = [[0, 2, 0, 0],
           [0, 0, 0, 0],
           [0, 2, 0, 0],
           [0, 0, 0, 0]]
         
    assert zero_matrix(matrix2) == res2

def test_rotate_matrix():
    matrix = [[1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4]]
    
    matrix2 = [[1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4]]
              
    res = [[2, 3, 4, 1],
           [4, 2, 2, 1],
           [4, 3, 3, 1],
           [4, 2, 3, 4]]
    
    assert rotate_matrix(matrix2) == res