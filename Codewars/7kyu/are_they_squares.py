"""
Write a function that checks whether all elements in an array are square numbers. The function should be able to take any number of array elements.
Your function should return true if all elements in the array are square numbers and false if not.
An empty array should return undefined / None / nil /false (for C). You can assume that all array elements will be positive integers.
"""


from typing import List
from math import isqrt


def is_square(arr: List[int]) -> bool:
    if not arr:
        return None
    
    squares: List[int] = [n for n in arr if isqrt(n)**2 == n]
    
    return len(squares) == len(arr)


print(is_square([1, 4, 9, 16, 7, 36]))