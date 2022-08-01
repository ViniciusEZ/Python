# In this kata, you have an input string and you
# should check whether it is a valid message.
# To decide that, you need to split the string by the
# numbers, and then compare the numbers with the number
# of characters in the following substring.
def is_a_valid_message(message):
    import re
    if message == '':
        return True
    if not message[0].isnumeric() or message[-1].isnumeric():
        return False
    pattern = re.findall(r'([0-9]+)([a-zA-Z]+)', message)
    for pair in pattern:
        if int(pair[0]) != len(pair[1]):
            return False
    return True

print(is_a_valid_message("2a1aa4aaaa"))