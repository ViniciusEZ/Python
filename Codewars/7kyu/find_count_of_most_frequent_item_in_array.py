"""
Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
"""


def most_frequent_item_count(collection):
    if not collection:
        return 0
    return collection.count(max(collection, key=collection.count))



print(most_frequent_item_count([1,1,1,1,3,4,5,7,7]))