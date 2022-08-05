# Implement String#digit?,
# which should return true if given object is a digit (0-9), false otherwise.


def is_digit(n):
    import re
    number = re.match(r'^\d$',n)
    return number is not None


print(is_digit('10'))