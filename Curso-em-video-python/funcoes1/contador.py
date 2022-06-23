from time import sleep


def count(p1, p2, p3):
    if p3 < 0:
        p3 *= -1
    if p3 == 0:
        p3 = 1
    if p1 < p2:
        print(f"Contagem de {p1} até {p2}, de {p3} em {p3}")
        for i in range(p1, p2 + 1, p3):
            print(i, end=' ')
            sleep(0.5)
    if p1 > p2:
        print(f"\nContagem de {p1} até {p2}, de {p3} em {p3}")
        for i in range(p1, p2 - 1, -p3):
            print(i, end=' ')
            sleep(0.5)


count(1, 10, 1)
count(10, 0, 2)
print("\n\nAgora é sua vez de personalizar a contagem: ")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
count(i, f, p)
