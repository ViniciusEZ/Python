# Shortranges
# \w -> [a-zA-Z0-9à-ú_]
# \w -> [a-zA-Z0-9_] -> re.A(ASCII)
# \W -> [^a-zA-Z0-9à-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
#  \D -> [^0-9]
# \s -> [ \r\n\f\t]
# \S ->  [^(vazio)\r\n\f\t]
# \b -> Bordas
# \B -> ^Bordas
import re

text = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# print(re.findall(r'[a-z]+',text, flags=re.I))
# print(re.findall(r'[a-z0-9]+',text, flags=re.I))
# print(re.findall(r'[a-z0-9à-ú]+',text, flags=re.I))
# print(re.findall(r'\w+',text))
# print(re.findall(r'\w+',text, re.A))
# print(re.findall(r'\W+',text))
# print(re.findall(r'\W+',text, re.A))
# print(re.findall(r'\d+',text))
# print(re.findall(r'\D+',text, re.I))
# print(re.findall(r'\s+',text))
# print(re.findall(r'\S+',text))
print(re.findall(r'\bflo\w+',text, re.I))
print(re.findall(r'\be\w+',text, re.I))
print(re.findall(r'\w+e\b',text, re.I))
print(re.findall(r'\b\w{4}\b',text, re.I))
print(re.findall(r'flo\B',text, re.I))
