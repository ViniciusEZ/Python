#Complete the function that returns an array of length n, 
#starting with the given number
#x and the squares of the previous number. 
#If n is negative or zero, return an empty array/list.

from typing import List

def squares(x, n) -> List[int]:
    squares: List[int] = [x] if n >= 1 else []
    for i in range(1,n):
        squares.append(squares[-1]**2)
             
    return squares


print(squares(3, 4))