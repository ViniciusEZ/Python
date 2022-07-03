# Given a number return the closest
# number to it that is divisible by 10.

def closest_multiple_10(i):
    return i - i % 10 if i % 10 < 5 else i - i % 10 + 10

print(closest_multiple_10(25))