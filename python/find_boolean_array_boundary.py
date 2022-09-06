"""
An array of boolean values is divided into two sections: the left section consists of all false, and the right section consists of all true. 
Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

Example#
Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.
"""

def find_boundary(arr):
    boundary_index = -1
    n = len(arr)
    if n == 0:
        return -1
    l = 0;
    r = n -1
    while l <= r:
        m = (l + r) // 2
        x = arr[m]
        if x:
            boundary_index = m
            r = m -1

        else:
            l = m +1
   
    return boundary_index