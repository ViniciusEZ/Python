"""
You will be given an array of numbers. You have to 
sort the odd numbers in ascending order while leaving the 
even numbers at their original positions.
"""

def sort_array(source_array):
    all_n = source_array
    odds = sorted([n for n in all_n if abs(n) % 2 != 0])
    for i in all_n:
        if abs(i) % 2 == 0:
            odds.insert(all_n.index(i), i)
            all_n[all_n.index(i)] = None
    return odds


print(sort_array([5, 3, 2, 8, 1, 4]))


print(abs(-34))

