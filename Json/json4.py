import json

with open('----------------------------------------') as f:
    player = json.load(f)

print(player['aeronaves'][0]['habilidade'])