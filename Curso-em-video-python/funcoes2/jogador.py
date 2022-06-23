def ficha(p1='<desconhecido>', p2=0):
    return print(f"O jogador {p1} marcou {p2} gol(s)")


jog = input("Nome do jogador: ")
gol = input("Gols marcados: ")
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(p2=gol)
else:
    ficha(jog, gol)


