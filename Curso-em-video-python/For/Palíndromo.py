user = str(input("Digite uma frase: ")).strip().lower()
palavra = user.split()
junto = ''.join(palavra)
inverso = ""

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

if inverso == junto:
    print("A frase é um palíndromo")
else:
    print("Não é um palíndromo: ")


