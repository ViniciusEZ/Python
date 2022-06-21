nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
med = round(((nota1 + nota2)/2), 2)

if med < 5:
    print(f"Sua média é: {med}\nVocê está REPROVADO!")
elif med <= 6.9:
    print(f"Sua média é: {med}\nVocê está de RECUPERAÇÃO!")
else:
    print(f"Sua média é: {med}\nVocê está APROVADO!")
