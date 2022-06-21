ida18 = 0
h = 0
m20 = 0

while True:
    print(20 * "-")
    print("CADASTRE UMA PESSOA.")
    print(20 * "-")
    ida = int(input("Digite a idade: "))
    if ida > 18:
        ida18 += 1
    sexo = input("Digite o sexo[M/F]: ").upper()
    print(20 * "-")
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and ida < 20:
        m20 += 1
    user = input("Deseja continuar? [S/N]").upper()
    if user == 'N':
        break
    else:
        pass
print(f"""Número de pessoas maiores de 18 anos: {ida18}.
Números de homens cadastrados: {h}.
Número de mulheres com idade menor que 20 anos: {m20}.""")