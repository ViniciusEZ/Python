user = int(input("Digite termos deseja mostrar? "))
t1 = 0
t2 = 1
c = 3
print(f"{t1} - {t2}", end='')

while c < user:
    t3 = t1 + t2
    print(f" - {t3}", end='')
    t1 = t2
    t2 = t3
    c += 1

print("\nFIM DA SEQUÊNCIA")

