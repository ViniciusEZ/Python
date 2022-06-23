def area(l, c):
    a = round(l * c, 2)
    return print(f"A aréa do seu terreno de {l} x {c} é {a}m².")


print("Controle de terrenos: ")
print("-" * 20)
lar = float(input("LARGURA(m): "))
com = float(input("COMPRIMENTO(m): "))
area(lar, com)
