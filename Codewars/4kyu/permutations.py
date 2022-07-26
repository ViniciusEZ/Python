# In this kata you have to create all permutations of a non empty input string and remove duplicates,
# if present. This means, you have to shuffle all letters from the input in all possible orders.


def permutations(s):
    from itertools import permutations
    per = [''.join(l) for l in permutations(s)]
    return list(set(per))

print(permutations('aabb'))