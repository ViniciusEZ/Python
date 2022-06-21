lista = ('Caneta', 1.60, 'Caderno', 10.00, 'Tesoura', 2.00, 'Lápis', 1.00, 'Cola', 3.00)
j = 0

print("LISTAGEM DE PREÇOS")
print(30*"=")
for c in range(0, len(lista)):
    print(f"{lista[j]} ............... R${lista[j+1]} ")
    j += 2
    if j == len(lista):
        break
print(30*"=")


