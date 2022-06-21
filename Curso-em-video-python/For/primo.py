user = int(input("Digite um número: "))
mult = 0

for c in range(2, user):
    if user % c == 0:
        print(f"múltiplo de: {c}")
        mult += 1

if mult == 0:
    print("É primo!")
else:
    print(f"Não é primo! O número é divisível por {mult} números")

