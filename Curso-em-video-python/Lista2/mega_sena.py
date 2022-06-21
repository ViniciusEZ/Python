from random import randint
from time import sleep
list = []
j = []
quantidade = int(input("Quantos jogos você deseja que eu sorteie: "))
t = 1

while t <= quantidade:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in list:
            list.append(n)
            c += 1
        if c >= 6:
            break
    list.sort()
    j.append(list[:])
    list.clear()
    t += 1

print(f"Sorteando {quantidade} jogos")
print(f"Os números sorteados foram: ")
for i, i2 in enumerate(j):
    print(f"Jogo {i+1}: {i2}")
    sleep(1)
print("Jogos sorteados! Programa finalizado!")