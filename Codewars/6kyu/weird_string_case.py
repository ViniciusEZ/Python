def to_weird_case(words):
    char = words.split(' ')
    weird = ''
    for ch in char:
        weird += ' '
        for i in range(0, len(ch)):
            if i % 2 == 0:
                weird += ch[i].upper()
            else:
                weird += ch[i].lower()
    return weird.strip()

print(to_weird_case('THIs iS a TEST'))