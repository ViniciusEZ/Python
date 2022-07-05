import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k,v in d1_json.items():
    print(f'{k}')
    for k1, v2 in v.items():
        print(f'{k1} - {v2}')