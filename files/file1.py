# r - read
# a - append
# w - write
# x - create
# t - text
# b - binary

import re

f = open("C:/Users/rifip/Documents/GitHub/Python/files/test.txt", "r")
# # txt = input('write a text: ')
# for l in f:
#     print(l)
# print(f.read())

res = re.sub(r"\s","-", f.readline())

f.close()

f = open("----------------------------------------------------------", "r")
# f.write(res)
print(f.read())
f.close()

