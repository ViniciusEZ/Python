user = float(input("Digite o valor do produto: R$"))

lis = ['Dinheiro/Cheque', 'À Vista', '2x no Cartão', '3x ou mais no Cartão']

for posicao, op in enumerate(lis):
    print(f"[{posicao+1}] - {op}")

user2 = int(input("Digite a opção de pagamento desejada: "))

if user2 == 1:
    print(f"O valor a ser pago é: R${user - (user * (10/100))}")
elif user2 == 2:
    print(f"O valor a ser pago é: R${user - (user * (5 / 100))}")
elif user2 == 3:
    print(f"O valor a ser pago é: R${user}")
elif user2 == 4:
    print(f"O valor a ser pago é: R${user + (user * (20 / 100))}")

