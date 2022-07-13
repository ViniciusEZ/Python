# Your task is to sort an array of integer numbers by the product of the value and the index of the positions.
# For sorting the index starts at 1, NOT at 0!
# The sorting has to be ascending.
# The array will never be null and will always contain numbers.

def sort_by_value_and_index(arr):
    i2 = 1
    i = 0
    list2 = []
    for index, value in enumerate(arr):
        list2.append((index+1) * value)
    list2 = sorted(list2)
    while i < len(list2):
        if arr[i2 - 1] * i2 == list2[i]:
            list2.insert(i, arr[i2 - 1])
            list2.remove(list2[i + 1])
            i2 += 1
            if i2 > len(list2):
                break
            i = 0
            continue
        i += 1
    return list2



print(sort_by_value_and_index([ 23, 2, 3, 4, 5 ]))

