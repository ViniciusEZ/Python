# Your task is to make two functions
# ( max and min, or maximum and minimum, etc., depending on the language )
# that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
def minimum(arr):
    mini = 0
    for i in range(0, len(arr)):
        if i == 0:
            mini = arr[i]
        if arr[i] < mini:
            mini = arr[i]
    return mini


def maximum(arr):
    maxi = 0
    for i in range(0, len(arr)):
        if i == 0:
            maxi = arr[i]
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi


print(maximum([0,1,2,3,4,5,6,7]))
print(minimum([89,2,5,7,23,76,100]))