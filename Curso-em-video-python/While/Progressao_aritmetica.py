pri = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
t = pri
c = 0
tot = 0
ter = 10


while ter != 0:
    tot += ter
    while c < tot:
        print(f"{t} ", end='')
        t += r
        c += 1
    print("Pausa!")
    ter = int(input("Quantos termos a mais você deseja mostrar? "))
print("\nPrograma finalizado!")


