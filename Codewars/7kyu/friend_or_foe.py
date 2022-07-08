# Make a program that filters a list of strings and
# returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can
# be sure that it has to be a
# friend of yours! Otherwise, you can be sure he's not...

def friend(x):
    return [f for f in x if len(f) == 4]


print(friend(['Ryan', 'Kieran', 'Mark']))