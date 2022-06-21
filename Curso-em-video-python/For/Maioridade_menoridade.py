from datetime import date

c = 1
ma = 0
me = 0
for i in range(1, 7):
    nasc = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    atual = date.today().year
    ida = atual - nasc
    if ida > 18:
        ma += 1
    else:
        me += 1
    c += 1

print(f"No grupo temos: {ma} maiores de idade e {me} menores de idade ")
