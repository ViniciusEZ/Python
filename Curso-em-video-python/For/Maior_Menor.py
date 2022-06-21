
maior = 0
menor = 0
for i in range(1, 6):
    user = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        maior = user
        menor = user
    else:
        if user > maior:
            maior = user
        elif user < menor:
            menor = user


print(f"O maior peso lido foi: {maior}KG")
print(f"O menor peso lido foi: {menor}KG")

