from random import randint
i = 0
j = 0
numeros = ()
maior = menor = 0

while i < 5:
    numeros += (randint(0, 100),)
    if i == 0:
        maior = menor = numeros[j]
    if numeros[j] > maior:
        maior = numeros[j]
    if numeros[j] < menor:
        menor = numeros[j]
    i += 1
    j += 1


print(numeros)
print(f"O maior valor da tupla é {maior} e o menor {menor}.")

