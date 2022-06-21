med1 = int(input("Digite a primeira medida: "))
med2 = int(input("Digite a segunda medida: "))
med3 = int(input("Digite a terceira medida: "))

if med1 > med2 + med3 or med2 > med1 + med3 or med3 > med1 + med2:
    print("Não é possível formar um triângulo!")
else:
    print("É possível formar um triângulo!")