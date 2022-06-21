c = 0
s = 0

user = int(input("Digite um número: "))

while user != 999:
    c += 1
    s += user
    user = int(input("Digite um número: "))

print(f"Você digitou {c} números e a somatória deles é {s}")
