# Complete the function that takes 3 numbers x, y and k (where x ≤ y), and returns the number of integers
# within the range [x..y] (both ends included) that are divisible by k
# .

def divisible_count(x,y,k):
    divisible = len([ndiv for ndiv in range(x, y+1) if ndiv % k == 0])
    return divisible

print(divisible_count(6,11,2))