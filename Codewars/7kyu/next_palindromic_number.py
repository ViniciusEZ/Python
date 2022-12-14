"""
In this kata you will be given a positive integer, 
val and you have to create the function next_pal()(nextPal Javascript) 
that will output the smallest palindrome number higher than val.
"""

def next_pal(val):
    p_palindrome = str(val+1)
    while p_palindrome != p_palindrome[::-1]:
        p_palindrome = str(int(p_palindrome)+1)
    return int(p_palindrome)


print(next_pal(11))