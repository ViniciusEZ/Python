exp = input("Digite a expressão: ")
paren = []

for sim in exp:
    if sim == '(':
        paren.append('(')
    elif sim == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break

if len(paren) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
