while True:
    user = int(input("\nDigite um valor para ver a sua tabuada(Zero para sair): "))
    if user == 0:
        break
    else:
        for i in range(1, 11):
            print(f"{user} x {i} = {user * i}")
print("Programa finalizado!")

