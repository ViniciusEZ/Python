"""
Given an unsorted array of integers, find the smallest number in the array, the
largest number in the array, and the smallest number between 
the two array bounds that is not in the array.
"""


def min_min_max(arr):
    min_element = min(sorted(arr))
    max_element = max(sorted(arr))
    for i in range(min_element, max_element):
        if i not in arr:
            middle_element = i
            break
    return [min_element, middle_element, max_element]

print(min_min_max([-1, 4, 5, -23, 24]))