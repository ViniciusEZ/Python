"""
Create the 
function that takes as a parameter a sequence 
of numbers represented as strings and outputs a sequence 
of numbers.
"""


def to_float_array(arr): 
    return [int(n) if n.isnumeric() else float(n) for n in arr]


print(to_float_array(["1.2", "2", "3"]))
