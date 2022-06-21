list = ('Macaco', 'Tabela', 'Galinha', 'Armario', 'Carro', 'Celular', 'Curso')
i = 0
j = 0
for c in range(0, len(list)):
    while i < len(list):
        if i < len(list):
            print(f"\nA palavra {list[i]} tem as seguintes vogais: ", end="")
            break
    if 'a' in list[i].lower():
        print(f"a", end=" ")
    if 'e' in list[i].lower():
        print(f"e", end=" ")
    if 'i' in list[i].lower():
        print(f"i", end=" ")
    if 'o' in list[i].lower():
        print(f"o", end=" ")
    if 'u' in list[i].lower():
        print(f"u", end=" ")
    i += 1

# Outro modo de fazer que, após um tempo, eu notei.
# Me senti meio burro de ter feito tudo aquilo na resolução anterior.

for palavra in list:
    print(f"\n\nA palavra {palavra} tem as seguintes vogais: ", end="\n")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")


