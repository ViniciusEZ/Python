def dont_give_me_five(start_, end_):
    n = 0
    return sum([n+1 for i in range(start_, end_+1) if '5' not in str(i)])


print(dont_give_me_five(4, 17))
