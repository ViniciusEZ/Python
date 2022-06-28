from pprint import pprint
from functools import reduce
_print = print
print = pprint


products = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
    {'nome': 'P5', 'preco': 33.22, 'peso_kg': 3.578, 'variacoes': ['i', 'j']},
    {'nome': 'P6', 'preco': 67.79, 'peso_kg': 9.920, 'variacoes': ['k', 'l']},
    {'nome': 'P7', 'preco': 45.31, 'peso_kg': 1.123, 'variacoes': ['m', 'n']},
    {'nome': 'P8', 'preco': 93.27, 'peso_kg': 0.521, 'variacoes': ['o', 'p']},
    {'nome': 'P9', 'preco': 1.90, 'peso_kg': 1.300, 'variacoes': ['q', 'r']},
]

# REDUCE
total_price = reduce(lambda total, preco: total + preco['preco'] , products, 0)
reduce_list_comprehension = round(sum([p['preco'] for p in products]))
print(round(total_price))
print(reduce_list_comprehension)

# MAP
# products_filter = list(filter(lambda price: price['preco'] > 20, products))
# products_filter_list_comprehension = [p['preco'] for p in products if p['preco'] > 20]
# print(products_filter)
# print('-='*40)
# print(products_filter_list_comprehension)

# FILTER_MAP
# products_filter_map = list(map(lambda p: p['preco'], filter(lambda price: price['preco'] > 20, products)))
# print(products_filter_map)

# MAP
# products_map = list(map(lambda price: price['preco'], products))
# products_map_list_comprehension = [product['preco'] for product in products]
# print(products_map)
# print(products_map_list_comprehension)

#prices = []
#for product in products:
#    prices.append(product['preco'])
#print(prices)
