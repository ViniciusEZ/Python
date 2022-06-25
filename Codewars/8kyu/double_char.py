# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
def double_char(s):
    i2 = ''
    for i in s:
        i2 += i * 2
    return i2


print(double_char("STRING"))
