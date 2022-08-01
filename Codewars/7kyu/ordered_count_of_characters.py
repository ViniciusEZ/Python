# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.
# For empty output return an empty list.

def ordered_count(inp):
    cont = []
    dupli = set()
    for l in inp:
        if l not in dupli:
            cont.append((l, inp.count(l)))
            dupli.add(l)
    return cont

print(ordered_count('abracadabra'))