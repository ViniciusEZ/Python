import os
import json

d1 = {
    "Pessoa 1": {
        "Name": "Luiz",
        "Age": 25,
    },
    "Pessoa 2": {
        "Name": "Rose",
        "Age": 53,
    }
}
print(d1)
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)

# with open('abc.txt', 'a+') as file:
#     file.write('Other line\n')
#     file.seek(0)
#     print(file.read())
#
#
# os.remove('abc.txt')

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# file.write('Line 1\n')
# file.write('Line 2\n')
# file.write('Line 3\n')
#
# file.seek(0, 0)
# print('Reading lines: ')
# print(file.read())
# print('-'*30)
#
# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('-'*30)
#
# file.seek(0,0)
# for linha in file:
#     print(linha, end='')


