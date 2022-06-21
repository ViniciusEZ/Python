ficha = list()

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    user = input("Quer continuar? [S/N]")
    if user.lower() == 'n':
        break

print('=' * 30)
print(f"{'N.':<4}{'NOME':<10}{'MÉDIA':>8}")
print('=' * 30)

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.2f}")

while True:
    print("=" * 30)
    opc = int(input("Mostrar o boletim de qual aluno? (999 interrompe)"))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")

print("PROGRAMA FINALIZADO!!!")
