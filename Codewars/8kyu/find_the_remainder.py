"""
Write a function that accepts two integers and 
returns the remainder of dividing the larger 
value by the smaller value.
Division by zero should return an empty value.
"""


def remainder(a,b):
    try:
        if b > a:
            a,b = b,a
        return divmod(a,b)[1]
    except ZeroDivisionError:
        return None

print(remainder(-1, 0))