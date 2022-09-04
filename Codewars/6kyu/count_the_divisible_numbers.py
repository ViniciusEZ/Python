# Complete the function that takes 3 numbers x, y and k (where x ≤ y), and returns the number of integers
# within the range [x..y] (both ends included) that are divisible by k
# .

def divisible_count(x, y, k):
    from math import floor
    return y // k - (x - 1) // k


print(divisible_count(6, 20, 2))
print(round(2.57,0))