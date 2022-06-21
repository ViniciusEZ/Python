soma = 0
mulheres20 = 0
maisvelho = ''
nomeV = ''

for i in range(1, 5):
    print(f"Digite as informações da {i}ª pessoa")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [M/F]: ").lower()
    print("="*50)
    if i == 1 and sexo == 'm':
        maisvelho = idade
        nomeV = nome
    elif sexo == 'm' and idade > maisvelho:
        maisvelho = idade
        nomeV = nome

    if sexo == 'f' and idade < 20:
        mulheres20 += 1

    soma += idade

media = round(float(soma / 4), 2)

print(f"A média das idades do grupo é: {media}")
print(f"O número de mulheres abaixo de 20 anos é: {mulheres20}")
print(f"O homem mais velho do grupo é: {nomeV}, {maisvelho}")
