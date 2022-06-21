from random import randint

user = int(input("Digite um número: "))
machine = randint(0, 10)

if user == machine:
    print("Você acertou!")
else:
    print("Você errou!")

print(f"O número correto é: {machine}")
