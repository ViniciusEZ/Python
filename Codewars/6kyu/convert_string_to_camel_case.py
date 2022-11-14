"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if 
the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.
"""
import re

def to_camel_case(text):
    camel = re.split(r'[-_]+', text)
    capitalized = []
    for word in camel[1:]:
        capitalized.append(word.capitalize())
    capitalized.insert(0, camel[0])
    return ''.join(capitalized)



print(to_camel_case('the_stealth_warrior'))