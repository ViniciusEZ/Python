user = input("Digite alguma coisa: ")
print(f"O número de vezes que a letra A aparece é: {user.count('a')}")
print(f"A primeira ocorrência da letra A é na posição: {user.find('a')+1}")
print(f"A última ocorrência da letra A é na posição: {user.rfind('a')+1}")

