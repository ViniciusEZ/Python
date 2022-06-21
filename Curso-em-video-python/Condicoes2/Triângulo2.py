med1 = int(input("Digite a primeira medida: "))
med2 = int(input("Digite a segunda medida: "))
med3 = int(input("Digite a terceira medida: "))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print("É possível formar um triângulo!")
    if med1 == med2 == med3:
        print("EQUILÁTERO")
    elif med1 != med2 != med3 != med1:
        print("ESCALENO")
    else:
        print("ISÓSCELES!")
else:
    print("Não é possível formar um triângulo!")


