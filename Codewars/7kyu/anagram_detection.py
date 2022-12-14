"""
Complete the function to return true if the two arguments given 
are anagrams of each other; return false otherwise.
"""

def is_anagram(test, original):
    if len(test) != len(original):
        return False
    anagram = test.upper()
    for i in anagram:
        if i not in original.upper():
            return False
        else:
            anagram.replace(anagram[anagram.index(i)], '')
    return True


print(is_anagram("foefet", "toffee"))

        


