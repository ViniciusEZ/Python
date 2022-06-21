vel = int(input("Digite a velocidade do carro: "))

if vel > 80:
    print(f"Você foi multado! O custo da multa é: R${(vel - 80) * 7}")
else:
    print("Velocidade na faixa recomendada!")
