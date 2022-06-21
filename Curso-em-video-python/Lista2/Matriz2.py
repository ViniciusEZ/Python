list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = 0
somaT = 0
maior = 0
for i in range(0, 3):
    for i2 in range(0, 3):
        list[i][i2] = int(input(f"Digite o número da posição [{i}] - [{i2}]: "))
        if list[i][i2] % 2 == 0:
            somaP += list[i][i2]
        if i2 == 2:
            somaT += list[i][i2]
        if list[1][i2] == 0:
            maior = list[1][i2]
        else:
            if list[1][i2] > maior:
                maior = list[1][i2]


print()


for i in range(0, 3):
    for i2 in range(0, 3):
        print(f"{list[i][i2]}", end=' ')
    print()
print(f"A soma de todos os números pares da matriz é: {somaP}")
print(f"A soma dos valores da terceira coluna é: {somaT}")
print(f"O maior valor da segunda linha é: {maior}")