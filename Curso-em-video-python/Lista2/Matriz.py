list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for i2 in range(0, 3):
        list[i][i2] = int(input(f"Digite o número da posição [{i}] - [{i2}]: "))

print()
for i in range(0, 3):
    for i2 in range(0, 3):
        print(f"{list[i][i2]}", end=' ')
    print()


