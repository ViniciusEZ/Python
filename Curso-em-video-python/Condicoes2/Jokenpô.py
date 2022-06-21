from random import choice
from time import sleep

lis = ['Pedra', 'Papel', 'Tesoura']

for posicao, op in enumerate(lis):
    print(f"[{posicao + 1}] - {op}")

user = int(input("Escolha: "))
mac = choice(range(1, 4))

if user == 1:
    print("Você escolheu Pedra!")
elif user == 2:
    print("Você escolheu Papel!")
elif user == 3:
    print("Você escolheu Tesoura!")
else:
    print("OPÇÃO INVÁLIDA!")

jogo = "JOKENPÔ!"
for i in jogo:
    print(i)
    sleep(1)

if mac == 1:
    print("A máquina escolheu Pedra!")
elif mac == 2:
    print("A máquina escolheu Papel!")
else:
    print("A maquina escolheu Tesoura!")


if user == mac:
    print("\nEMPATE!")
elif user == 1 and mac == 2:
    print("\nA máquina ganhou!")
elif user == 1 and mac == 3:
    print("\nVocê ganhou!")
elif user == 2 and mac == 1:
    print("\n Você ganhou!")
elif user == 2 and mac == 3:
    print("\nA máquina ganhou!")
elif user == 3 and mac == 1:
    print("\nA máquina ganhou!")
else:
    print("\nVocê ganhou!")


