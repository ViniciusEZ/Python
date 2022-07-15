int_numbers_list = [
    [1, 2, 3, 5, 6, 7, 7, 10, 9, 4],
    [5, 8, 10, 2, 6, 9, 4, 10, 9, 6],
    [8, 9, 6, 1, 4, 2, 3, 5, 7, 0, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 1, 6, 7, 8, 9, 10],
    [10, 2, 3, 4, 1, 6, 7, 8, 9, 0],
    [1,2,3,3,2,1]
]


def first_duplicate(arr):
    numbers = set()
    duplicate_number = -1
    for n in arr:
        if n in numbers:
            duplicate_number = n
            numbers.clear()
        numbers.add(n)

    return duplicate_number


for lists in int_numbers_list:
    print(f'{lists} {first_duplicate(lists)}')
