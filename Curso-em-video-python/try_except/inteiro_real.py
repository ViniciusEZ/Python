def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO. Digite um número inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário!")
            return 0
        else:
            return n


def real(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO. Digite um número inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário!")
            return 0
        else:
            return n


n = inteiro("Digite um número inteiro: ")
n1 = real("Digite um número real: ")
print(n)
print(n1)