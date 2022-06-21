from time import sleep

user = int(input("Digite um número para a contagem regressiva: "))
for i in range(user, 0, -1):
    print(i)
    sleep(0.5)

print("FOGO!")
