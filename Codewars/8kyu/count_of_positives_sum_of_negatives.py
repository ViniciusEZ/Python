# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the
# second element is sum of negative numbers.
# 0 is neither positive nor negative.

def count_positives_sum_negatives(arr):
    c = 0
    sum = 0
    for i in arr:
        if i > 0:
            c += 1
        else:
            sum += i
    return [c, sum] if len(arr) > 0 else []

print(count_positives_sum_negatives([1,3,4,6,7,-1,-9,6]))