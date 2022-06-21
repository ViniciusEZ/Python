user = int(input("Digite seu salário: "))

if user > 1250:
    print(f"O seu salário com o aumento será de: {user + (user * (10/100))}")
else:
    print(f"O seu salário com o aumento será de: {user + (user * (15 / 100))}")
