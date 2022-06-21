list = []
i = 0
while True:
    user = int(input("Digite um número: "))
    for c in range(0, len(list)):
        if user not in list:
            print("Valor registrado!")
            list.append(user)
            break
        else:
            print("Valor já registrado! Não será adicionado.")
            break
    if len(list) == 0:
        list.append(user)
        print("Valor registrado!")
    user1 = input("Deseja continuar? [S/N]")
    if user1.upper() == 'N':
        break

print(sorted(list))