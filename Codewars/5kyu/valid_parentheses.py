# Write a function that takes a string of parentheses, and determines
# if the order of the parentheses is valid. The function should return true if the
# string is valid, and false if it's invalid.

def valid_parentheses(string):
    pile = []
    for paren in string:
        if paren == '(':
            pile.append('(')
        elif paren == ')':
            if len(pile) > 0:
                pile.pop()
            else:
                pile.append(')')
                break
    return len(pile) == 0

print(valid_parentheses("(())((()())())"   ))
