def leiadinheiro(msg):
    ok = False
    while not ok:
        entry = str(input(msg)).replace(',', '.')
        if entry.isalpha() or entry.strip() == '':
            print(f"ERRO. \"{entry}\" é um preço inválido!")
        else:
            ok = True
            return float(entry)


