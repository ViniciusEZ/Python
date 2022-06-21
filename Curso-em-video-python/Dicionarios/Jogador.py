partidas = {}
partidas['Nome'] = input("Nome do jogador: ")
p = int(input(f"Quantas partidas {partidas['Nome']} jogou? >>>"))
total = 0
gol = []

for i in range (0, p):
    gol.append(int(input(f"Quantidade de gols na partida {i+1}: ")))
    total += gol[i]
partidas['Gol'] = gol
partidas['Total'] = total

print("-=" * 30)
print(partidas)
print("-=" * 30)

for k, v in partidas.items():
    print(f"{k} é {v}")
print("-=" * 30)

print(f"O jogador {partidas['Nome']} jogou {p} partidas.")
for c in range(0, p):
    print(f" - Na partida {c+1}, marcou {gol[c]} gols")
print(f"Um total de {partidas['Total']} gols.")

