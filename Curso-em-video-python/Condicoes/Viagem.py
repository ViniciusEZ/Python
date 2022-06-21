user = int(input("Digite a distância da viagem em quilômetros: "))

if user > 200:
    print(f"O preço da viagem será: R${user * 0.45}")
else:
    print(f"O preço da viagem será: R${user * 0.50}")

