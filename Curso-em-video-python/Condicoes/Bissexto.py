user = int(input("Digite um ano: "))

if user % 4 == 0 and user % 100 == 0 and user % 400 == 0:
    print("É ano bissexto!")
elif user % 4 != 0 and user % 100 != 1:
    print("Não é ano bissexto!")
elif user % 4 == 0:
    print("É ano bissexto!")
