"""Write a method, that will get an integer array as parameter and will process 
every number from this array.
Return a new array with processing every number of the input-array like this:
If the number has an integer square root, take this, otherwise square the number.
"""

def square_or_square_root(arr):
    return [int(n**(1/2)) if (n**(1/2)).is_integer() else n**2 for n in arr]


print(square_or_square_root([100, 101, 5, 5, 1, 1]))



