bases = ['Binário', 'Octal', 'Hexadecimal']

for posicao, op in enumerate(bases):
    print(f"[{posicao+1}] - {op}")

user = int(input("Digite o número da opção desejada: "))

if user == 1:
    num = int(input("""\nSeu número será convertido para binário!
Digite o número: """))
    print(bin(num).replace("0b", ""))
elif user == 2:
    num = int(input("""\nSeu número será convertido para octal!
Digite o número: """))
    print(oct(num))
elif user == 3:
    num = int(input("""\nSeu número será convertido para hexadecimal!
Digite o número: """))
    print(hex(num))



