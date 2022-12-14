"""
For example, if we run 9119 through the function, 811181 will come out, because 9 is 81 and 1 is 1.
"""

def square_digits(num):
    return int(''.join([str(int(n)**2) for n in str(num)]))


print(square_digits(0))