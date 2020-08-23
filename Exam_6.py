import math
"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    l_value = 0
    r_value = len(input_array)-1
    m_value = int(math.ceil(len(input_array)/2) -1)
    while m_value <  len(input_array)-1  and m_value > 0:                      
        if input_array[m_value] == value:
            return m_value
        elif input_array[m_value] > value:
            if m_value -1 < 0:
                return -1
            r_value =  m_value -1
            if r_value == l_value:
                m_value = r_value
            else:
                m_value = int(math.ceil((r_value - l_value) / 2))
        else:
            l_value =  m_value +1
            if r_value == l_value:
                m_value = r_value
            else:
                m_value = r_value - l_value + m_value   
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))