"""
See this property again: 135 = 1^1 + 3^2 + 5^3
We need a function to collect these numbers, that may receive two integers 
aaa, bbb that defines the range [a,b][a, b][a,b] (inclusive) and outputs a 
list of 
the sorted numbers in the range that fulfills the property described above.
"""

def sum_dig_pow(a, b): 
    sum_p = 0
    list_p = []
    nums = {str(i) for i in range(a, b+1)}
    for n in nums:
        for i, v in enumerate(n):
            sum_p += int(v) ** (i+1)
        if sum_p == int(n):
            list_p.append(int(n))
        sum_p = 0
    return sorted(list_p)
            
    


print(sum_dig_pow(89, 135))