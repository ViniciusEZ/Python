def password(passcode):
    import re
    return bool(re.search(r'^(?=[a-zA-Z0-9]*[a-z]+)(?=[a-zA-Z0-9]*[A-Z]+)(?=[a-zA-Z0-9]*\d+)(?!.+\s+)(?!.*[ -/:-@[-`{-~]+).{6,}$', passcode, re.A))


print(password('fjd3IR9dsa3'))



