# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
def repeat_str(repeat, string):
    return f'{string}' * repeat

repeat_str(3, 'hello ')