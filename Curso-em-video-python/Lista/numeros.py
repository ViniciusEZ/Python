list = []
quantn = 0
while True:
    user = int(input("Digite um número: "))
    list.append(user)
    quantn += 1

    user1 = input("Deseja continuar? [S/N]")
    if user1.upper() == 'N':
        break

print(f"Você digitou {quantn} números!")
list.sort(reverse=True)
print(f"A lista dos valores em ordem decrescente: {list}")
if 5 in list:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")




