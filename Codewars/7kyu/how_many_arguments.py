"""
Create a function args_count, that returns the count of passed arguments
"""

def args_count(*args, **kwargs):
    return len(args) + len(kwargs)


print(args_count(100, 2, 3))