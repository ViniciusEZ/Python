# You are given two sorted arrays that both only contain integers.
# Your task is to find a way to merge them into a single one, sorted in asc order.
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

def merge_arrays(arr1, arr2):
    list = []
    for i in arr1:
        list.append(i) if i not in list else 1
    for i2 in arr2:
        list.append(i2) if i2 not in list else 1
    return sorted(list)