"""
Complete the function that takes a sequence of numbers as single parameter. 
Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.

The input is a sequence of numbers: integers and/or floats.
"""

def sum_even_numbers(seq): 
    return sum([n for n in seq if n % 2 == 0])


print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))