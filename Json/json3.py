import json
#
# jogador = {
#     'nome': 'Bruno',
#     'time': 'aviadores',
#     'vivo': True,
#     'energia': 100,
#     'mochila': ['pederneira', 'corda', 'linha', 'arame'],
#     'aeronaves': [
#         {'tipo': 'transporte', 'habilidade': 80},
#         {'tipo': 'ataque', 'habilidade': 100},
#         {'tipo': 'reconhecimento', 'habilidade': 50}
#         ]
# }

player_j = '{"nome": "Bruno","time": "aviadores","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronaves": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100}, {"tipo": "reconhecimento", "habilidade": 50}]}'

player = json.loads(player_j)
print(player)

# for c in player:
#     print(c)

print(player['aeronaves'][0]['habilidade'])
