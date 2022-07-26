# Find the sum of the digits of all the numbers from 1 to N (both ends included).

def compute_sum(n):
    s = 0
    for number in range(0, n+1):
        if number <= 9:
            s += number
        else:
            number = str(number)
            for n1 in number:
                s += int(n1)
    return s

print(compute_sum(12))
