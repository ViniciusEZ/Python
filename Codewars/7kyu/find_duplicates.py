# Given an array, find the duplicates in that array, and return a new array of those duplicates.
# The elements of the returned array should appear in the order when they first appeared as duplicates

def duplicates(array):
    n_duplicates = []
    set1 = set()
    for n in array:
        if n in set1:
            n_duplicates.append(n)
            set1.remove(n)
            continue
        set1.add(n)
    for i in range(0, len(n_duplicates)):
        for i2 in range(i + 1, len(n_duplicates)):
            if i2 == len(n_duplicates):
                break
            if n_duplicates[i] == n_duplicates[i2]:
                n_duplicates.remove(n_duplicates[i2])
    return n_duplicates


print(duplicates([-2, 6, 1, -2, 3, 10, 9, -2, 3, -4, -8, -3, 6, -2, 0, 6, 0, -4]))
