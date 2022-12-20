"""
Complete the function that accepts a valid string and returns an integer.
Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, 
then the result should be the sum of the numbers in the hex strings (ignore letters).
"""
import re

def hex_hash(code):
    list_hex = [re.sub(r'[A-Za-z0]+','', str(hex(ord(c)))) for c in code]
    sum = 0
    for i in list_hex:
        if len(i) > 1:
            for n in i:
                sum += int(n)
        else:
            sum += int(i)
    return sum


print(hex_hash("Forty4Three"))