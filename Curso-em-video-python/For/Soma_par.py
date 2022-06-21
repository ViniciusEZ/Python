s = 0
for i in range(0, 6):
    user = int(input("Digite um número: "))
    if user % 2 == 0:
        s += user

print(f"O resultado da somatória dos números pares foi: {s}")

