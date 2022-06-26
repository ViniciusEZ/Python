# Given three integers a ,b ,c, return the largest number obtained
# after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

def expression_matter(a, b, c):
    list = [a * (b + c),
            a * b * c,
            a + b + c,
            a + b * c,
            (a + b) * c,
            a * b + c]
    return max(list)


print(expression_matter(1,1,1))