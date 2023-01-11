"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!
"""

def find_uniq(arr):
    from collections import Counter
    count = Counter(arr)
    return min(count, key=count.get)


print(find_uniq([ 3, 10, 3, 3, 3 ]))