import json

cars_dictionary = {
    'marca': 'Honda',
    'modelo': 'HRV',
    'cor': 'Prata'
}

cars_list = ['Honda', 'Volkswagem', 'Ford', 'Fiat', 'Chevrolet']

cars_tuple = ('Honda', 'Volkswagem', 'Ford', 'Fiat', 'Chevrolet')

cars_j = json.dumps(cars_dictionary, indent=4,separators=(": ","= "),sort_keys=True)
print(cars_j)
