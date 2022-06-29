# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

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

print(re.findall(r'João|Maria|ad....s', text))
print(re.findall(r'João|joão|Maria|ad....s', text))
print(re.findall(r'[Jj]oão|[Mm]aria|ad....s', text))
print(re.findall(r'[a-z]aria', text))
print(re.findall(r'[a-zA-Z]oão|[a-zA-Z]aria', text))
print(re.findall(r'JOão|mARiA', text, flags=re.I))






