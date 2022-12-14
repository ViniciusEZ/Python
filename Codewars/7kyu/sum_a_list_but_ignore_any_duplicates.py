"""
Please write a function that sums a list, 
but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , 
the function should return 10.
"""

def sum_no_duplicates(l):
    return sum([n for n in l if l.count(n) == 1])


print(sum_no_duplicates([1, 1, 2, 2, 3]))