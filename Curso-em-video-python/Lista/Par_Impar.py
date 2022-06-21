list = []
par = []
impar = []
while 1:
    user = int(input("Digite um número: "))
    list.append(user)
    user1 = input("Deseja continuar? [S/N]")
    if user1.lower() == 'n':
        break

for i in range(0, len(list)):
    if list[i] % 2 == 0:
        par.append(list[i])
    else:
        impar.append(list[i])

print(f"Lista dos números digitados: {list}")
print(f"A lista contendo apenas números pares: {par}")
print(f"A lista contendo apenas números ímpares: {impar}")
