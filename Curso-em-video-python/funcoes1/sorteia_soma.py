from random import randint
from time import sleep


def sorteia(lst):
    for i in range(1, 6):
        lst.append(randint(0, 100))
    print("Sorteando 5 valores: ", end='')
    for i in lst:
        print(f"{i}", end=' ')
        sleep(0.5)


def somapar(lst):
    somap = 0
    for i in lst:
        if i % 2 == 0:
            somap += i
    print(f"\nSomando os valores pares de {lst}, temos {somap}")


lista = []
sorteia(lista)
somapar(lista)
