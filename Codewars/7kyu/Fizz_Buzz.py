# Return an array containing the numbers from 1 to N, where N is the parametered value.
#
# Replace certain values however if any of the following conditions are met:
#
#     If the value is a multiple of 3: use the value "Fizz" instead
#     If the value is a multiple of 5: use the value "Buzz" instead
#     If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
#
# N will never be less than 1.

def fizzbuzz(n):
    return ["Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0) or num for num in range(1, n+1)]


def fizzbuzz2(n):
    listfb = []
    for num in range(1, n):
        if num % 15 < 1:
            listfb.append('FizzBuzz')
        elif num % 3 < 1:
            listfb.append('Fizz')
        elif num % 5 < 1:
            listfb.append('Buzz')
        else:
            listfb.append(num)
    return listfb


print(fizzbuzz(15))
print(fizzbuzz2(15))
