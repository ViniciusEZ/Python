c = s = 0

while True:
    user = int(input("Digite um número(999 para parar): "))
    if user == 999:
        break
    else:
        s += user
        c += 1

print(f"A quantidade de números digitados foi {c} e a soma entre ele é {s}")