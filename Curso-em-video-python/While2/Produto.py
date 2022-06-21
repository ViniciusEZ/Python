menor = barato = mil = ptotal = 0

while True:
    print(20 * "-")
    prod = input("Digite o nome do produto: ")
    p = int(input("Digite o preço do produto: R$"))
    print(20 * "-")
    ptotal += p
    if p > 1000:
        mil += 1
    if menor == 0:
        menor = p
    if p < menor:
        menor = p
        barato = prod
    user = input("Deseja continuar?[S/N] ").upper()
    if user == 'N':
        break

print(f"""O total gasto na compra: {ptotal}.
Número de produtos com preço maior que R$1000: {mil}.
Produto mais barato é {barato} que custa R${menor}.""")






