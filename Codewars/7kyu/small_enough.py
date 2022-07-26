# You will be given an array and a limit value. You must check that all values in the array
# are below or equal to the limit value. If they are, return true. Else, return false.


def small_enough(array, limit):
    small = [n for n in array if n <= limit]
    return len(small) == len(array)

print(small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100))

