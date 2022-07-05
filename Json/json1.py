import json

cars = {"marca": "Honda",
        "modelo": "HRV",
        "cor": "Prata"}


carros_json = json.dumps(cars)

print(carros_json)

# cars = json.loads(cars_json)
#
# print(cars)
#
# for x, y in cars.items():
#     print(f'{x}: {y}')