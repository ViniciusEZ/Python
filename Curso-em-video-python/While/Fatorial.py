user = int(input("Digite o número para calcular o seu fatorial: "))
n = user
fat = 1

while n > 0:
    print(f"{n}", end='')
    print(" x " if n > 1 else f" = {fat}", end='')
    fat *= n
    n -= 1

print(f"\nO fatorial de {user} é {fat}")

