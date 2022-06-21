from random import randint

print("A máquina adivinhará um número! Será que você consegue acertar?")
user = int(input("\nDigite um número: "))
n = 0
mac = 0

while user != mac:
    mac = randint(0, 10)
    print("Errou!")
    user = int(input("Digite um número: "))
    n += 1

print(f"ACERTOU! {n} tentativas até acertar!")