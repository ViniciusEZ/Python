def validate_usr(username):
    import re
    return bool(re.search(r'^((?=.*\d*)(?=.*[a-z]*)(?=.*_*)(?!.*[A-Z])+(?!.*\s)+(?!.*[!-.])+(?!.*[:-@])+)+.{4,16}$', username))


def validate(username):
    import re
    return re.match('^[a-z0-9_]{4,16}$', username) != None


print(validate('_____'))