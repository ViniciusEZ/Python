numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
'Dezenove', 'Vinte')
j = 0
user = int(input("Digite um número entre Zero e Vinte: "))

while user > 20 or user < 0:
    print("Tente Novamente!")
    user = int(input("Digite um número entre zero e vinte: "))


while user != numeros[j]:
    if user == j:
        break
    j += 1
print(f"Você digitou o número {numeros[j]}")



