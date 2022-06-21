pessoa = {}
dados = []
somaIda = totalP = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = input("Digite seu nome: ")
    while True:
        pessoa['Sexo'] = input("Sexo[M/F]: ").upper()
        if pessoa['Sexo'] == 'F' or pessoa['Sexo'] == 'M':
            break
        else:
            print("Digite somente M ou F!")
    while True:
        pessoa['Idade'] = int(input("Idade: "))
        somaIda += pessoa['Idade']
        if pessoa['Idade'] > 0:
            break
        else:
            print("A idade deve ser maior que 0!")
    dados.append(pessoa.copy())
    totalP += 1
    user = input("Quer continuar? [S/N]")
    if user.upper() == 'N':
        break

media = somaIda / totalP
print(f"O números de pessoas cadastradas foram: {totalP}")
print(f"A média de idade do grupo é {media:.2f}")
print("As mulheres cadastradas foram: ", end='')
for i in range(0, len(dados)):
    if dados[i]['Sexo'] == 'F':
        print(f"[{dados[i]['Nome']}]", end=' ')
print("\nLista de pessoas acima da média: ")
for c in dados:
    if c['Idade'] > media:
        for k, v in c.items():
            print(f"{k} = {v};", end=' ')
    print()
print("Programa encerrado!")
