list = []
maior = menor = 0

for i in range(0, 5):
    user = int(input(f"Digite um valor: "))
    list.append(user)
    if i == 0:
        menor = maior = user
    if list[i] > maior:
        maior = list[i]
    if list[i] < menor:
        menor = list[i]

print(f"Você digitou os seguintes valores: {list}")
print(f"O maior valor digitado foi [{maior}] nas posições: ", end="")
for c, d in enumerate(list):
    if maior == d:
        print(f"[{c+1}]", end=" ")
print(f"\nO menor valor digitado foi [{menor}] nas posições: ", end="")
for c, d in enumerate(list):
    if menor == d:
        print(f"[{c+1}]", end=" ")


