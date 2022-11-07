#When provided with a String, capitalize all vowels


import re
from typing import List

def swap(st) -> str:
    capitalized: List[str] = []
    for l in st:
        if re.findall(r'[aeiou]', l):
            capitalized.append(l.upper())
        else:
            capitalized.append(l)
    return ''.join(capitalized)


print(swap("HelloWorld!"))
        



