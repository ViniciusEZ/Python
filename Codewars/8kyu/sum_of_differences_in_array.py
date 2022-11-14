def sum_of_differences(arr):
    if not arr or len(arr) == 1:
        return 0
    s_arr = sorted(arr, reverse=True)
    dif = []
    for i in range(len(s_arr)):
        try:
            dif.append(s_arr[-2] - s_arr[-1])
            s_arr.pop()
        except IndexError:
            break
    return sum(dif)
    
    
print(sum_of_differences([-3, -2, -1]))
    
    
    