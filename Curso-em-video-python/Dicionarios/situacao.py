aluno = {}

aluno['Nome'] = input("Nome: ")
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
elif 4 <= aluno['Média'] <= 5.9:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] < 4:
    aluno['Situação'] = 'Reprovado'

print()
for k, v in aluno.items():
    print(f"{k} é {v}")




