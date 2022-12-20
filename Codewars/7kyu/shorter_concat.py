"""
Given 2 strings, a and b, return a string of the form: 
shorter+reverse(longer)+shorter.

In other words, the shortest string has to be put as 
prefix and as suffix of the reverse of the longest.
"""
def shorter_reverse_longer(a,b):
    if len(a) == len(b):
        return f'{b}{a[::-1]}{b}'
    
    shorter = min(a,b, key=lambda x: len(x))
    longer = max(a,b, key=lambda x: len(x))
    
    return f'{shorter}{longer[::-1]}{shorter}'

print(shorter_reverse_longer("first", "abcde"))