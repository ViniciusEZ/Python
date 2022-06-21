user = "S"
maior = menor = user1 = c = s = 0

while user == "S":
    user1 = int(input("Digite um número: "))
    s += user1
    c += 1
    if c == 1:
        menor = maior = user1
    else:
        if user1 > maior:
            maior = user1
        elif user1 < menor:
            menor = user1
    user = str(input("Deseja continuar? [S/N] ")).upper()


print(f"A média dos valores lidos é {s / c} e o maior valor lido foi {maior} e o menor {menor}")

