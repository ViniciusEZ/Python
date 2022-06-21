dados = []
pessoas = []
maior = menor = 0
total = 0
while True:
    dados.append(input("Digite seu nome: "))
    dados.append(int(input("Digite seu peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    user = input("Deseja continuar?[S/N]")
    if user.upper() == 'N':
        break

print(f"Você cadastrou {total} pessoas.")
print(f"O maior peso foi {maior}Kg. Peso das pessoas: ", end='')
for c in pessoas:
    if c[1] == maior:
        print(f"[{c[0]}]", end=' ')
print(f"\nO menor peso foi {menor}Kg. Peso das pessoas: ", end='')
for c in pessoas:
    if c[1] == menor:
        print(f"[{c[0]}]", end=' ')




