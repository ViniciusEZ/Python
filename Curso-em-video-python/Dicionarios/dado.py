from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)
}
ranking = {}

print("Valores sorteados: ")
for k, v in jogadores.items():
    print(f"O {k} tirou: {v} no dado")
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
print("Ranking dos jogadores: ")
for i, k in enumerate(ranking):
    print(f"{i+1}º lugar: {k[0]} que tirou {k[1]} no dado")
