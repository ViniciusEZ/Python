import re

string = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1
Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''

print(re.findall(r'^[+-]?\d+(?:\.\d+)?(?:\,\d+)?$', string, re.M))

def is_float(n):
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?(?:,\d+)?$', n))

def is_int(n):
    return bool(re.search(r'^[+-]?\d+$', n))

print(is_float('-23.45'))
print(is_int('+2'))


while True:
    num = input('Digite um número: ')

    if is_int(num):
        num = int(num)
        print(f'O número {num} foi convertido para inteiro!')
        break
    if is_float(num):
        num = float(num)
        print(f'O número {num} foi convertido para flutuante!')
        break