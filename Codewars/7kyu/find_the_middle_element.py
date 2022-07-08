# As a part of this Kata, you need to create
# a function that when provided with a triplet,
# returns the index of the numerical element that
# lies between the other two elements.

def gimme(input_array):
    for i in input_array:
        if i < max(input_array) and i > min(input_array):
            return input_array.index(i)



