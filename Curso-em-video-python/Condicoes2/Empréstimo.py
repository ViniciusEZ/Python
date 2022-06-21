casa = int(input("Digite o valor da casa: R$"))
salario = int(input("Digite o valor do seu salário: R$"))
anos = int(input("Digite em quantos anos pagará: R$"))

prest = casa / (anos * 12)
mini = salario * (30/100)

if prest > mini:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO PODE SER CONCEDIDO!")

