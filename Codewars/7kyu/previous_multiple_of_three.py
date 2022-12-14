"""
Given a positive integer n: 0 < n < 1e6, remove the 
last digit until you're left with a number that is a 
multiple of three.

Return n if the input is already a multiple of three, 
and if no such number exists, 
return null, a similar empty value, or -1.
"""


def prev_mult_of_three(n):
    div = str(n)
    for i in range(n):
        if div:
            if int(div) % 3 == 0:
                return int(div)
            else:
                div = div[:-1]
    return None


print(prev_mult_of_three(952406))