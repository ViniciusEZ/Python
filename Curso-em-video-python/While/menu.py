op = 0

while op != 5:
    num1 = int(input("\nDigite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("""[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Dividir
[5] - Sair do programa""")
    op = int(input("\nDigite a opção desejada: "))

    if op == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == 4:
        print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
    elif op == 5:
        print("Programa encerrado!")

