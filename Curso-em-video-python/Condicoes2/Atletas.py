from datetime import date

nasc = int(input("Digite seu ano de nascimento: "))
ida = date.today().year - nasc

print(f"Você possui {ida} anos")

if ida <= 9:
    print("Sua categoria é: MIRIM.")
elif ida <= 14:
    print("Sua categoria é: INFANTIL.")
elif ida <= 19:
    print("Sua categoria é: JUNIOR.")
elif ida == 25:
    print("Sua categoria é: SÊNIOR.")
else:
    print("Sua categoria é: MASTER.")