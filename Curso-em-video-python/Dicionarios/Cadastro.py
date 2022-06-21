from datetime import datetime
pessoa = {}
pessoa['Nome'] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CTPS'] = int(input("Carteira de trabalho(0 para o caso de não ter): "))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input("Ano de contratação: "))
    pessoa['Salário'] = input("Salário: ")
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - datetime.now().year)
    print(pessoa)
    for k, v in pessoa.items():
        print(f"- {k} é {v}")
else:
    print(pessoa)
    for k, v in pessoa.items():
        print(f"- {k} é {v}")
