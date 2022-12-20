"""
Given an input of an array of digits, return the array with each digit incremented 
by its position in the array: the first digit will be incremented by 1, 
the second digit by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).

Your result can only contain single digit numbers, so if adding a digit with its 
position gives you a multiple-digit number, only the last digit of the number should be returned.
"""


def incrementer(nums):
    return [n + (v+1) if len(str(n + (v+1))) == 1 else int(str(n + (v+1))[-1]) for v, n in enumerate(nums)]


print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]))