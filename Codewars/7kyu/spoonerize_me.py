"""
Your task is to create a function that takes a 
string of two words, separated by a space: words and returns a spoonerism of those words in a string
"""

def spoonerize(words):
    spoon = words.split(' ')
    w1 = list(spoon[0])
    w2 = list(spoon[1])
    w1[0], w2[0] = w2[0], w1[0]
    spoon = w1 + [' '] + w2
    return ''.join(spoon)

print(spoonerize("pop corn"))


