partidas = {}
time = []

while True:
    partidas.clear()
    partidas['Nome'] = input("Nome do jogador: ")
    p = int(input(f"Quantas partidas {partidas['Nome']} jogou? >>>"))
    total = 0
    gol = []

    for i in range (0, p):
        gol.append(int(input(f"Quantidade de gols na partida {i+1}: ")))
        total += gol[i]
    partidas['Gol'] = gol
    partidas['Total'] = total
    time.append(partidas.copy())
    user = input("Quer continuar? [S/N]").upper()
    if user == 'N':
        break

print("cod ", end='')
for i in partidas.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k+1:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
while True:
    busca = int(input("Mostrar os dados de qual jogador? "))
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO!")
    else:
        print(f"Levantamento dos dados do jogador {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gol']):
            print(f" No jogo {i+1} fez {g} gols.")

