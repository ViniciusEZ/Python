p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))
imc = round(p / (a ** 2), 2)

if imc < 18.5:
    print(f"Seu IMC é: {imc} e você está ABAIXO DO PESO!")
elif imc < 25:
    print(f"Seu IMC é: {imc} e você está no PESO IDEAL!")
elif imc < 30:
    print(f"Seu IMC é: {imc} e você está com SOBREPESO!")
elif imc < 40:
    print(f"Seu IMC é: {imc} e você está com OBESIDADE!")
else:
    print(f"Seu IMC é: {imc} e você está com OBESIDADE MÓRBIDA!")
