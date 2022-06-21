list = [[], []]
for c in range(0, 7):
    user = int(input(f"Digite o {c+1}º número: "))
    if user % 2 == 0:
        list[0].append(user)
    else:
        list[1].append(user)

print(f"Os números pares digitados foram: {sorted(list[0])}")
print(f"Os números ímpares digitados foram: {sorted(list[1])}")
