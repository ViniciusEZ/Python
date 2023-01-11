"""
Write a function that given, an array arr,
returns an array containing at each index i 
the amount of numbers that are smaller than arr[i] to the right.
"""

def smaller(arr):
    smaller_counter = [len([x for x in arr[-i:] if x < arr[-i]]) for i in range(1, len(arr)+1)]
    return list(reversed(smaller_counter))


print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))
