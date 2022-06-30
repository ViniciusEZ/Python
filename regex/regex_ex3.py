# Meta caracteres:  ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}
import re

text = '''
<p>text 1</p> <p>Whatever</p> <p>Eita</p> <div></div>
'''
print(re.findall(r'<[pdiv]{1,3}>.*</[pdiv]{1,3}>', text))
print(re.findall(r'<[pdiv]{1,3}>.*?</[pdiv]{1,3}>', text))
print(re.findall(r'</*[pdiv]{1,3}>.*?', text))
print(re.findall(r'<[pdiv]{1,3}>.+?</[pdiv]{1,3}>', text))


