t = ()
n9 = 0
j = 0
c = 0

for i in range(0, 4):
    user = int(input("Digite um número: "))
    if user == 9:
        n9 += 1
    t += (user, )

print(f"O número 9 apareceu {n9} vez(es).")

for i in range(0, len(t)):
    if 3 == t[j]:
        print(f"O primeiro número 3 está na {j+1}º posição.")
        break
    j += 1

j = 0
print("Os números pares digitados foram: ")
while c < 4:
    if t[j] % 2 == 0:
        print(f"{t[j]}", end=" ")
    c += 1
    j += 1


