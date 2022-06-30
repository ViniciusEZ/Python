# Flags
# re.A -> ASCII
# re.I -> IGNORECASE
# re.M - MULTILINE -> ^$
# re.S -> Dotall

import re
text = '''
321.432.654-14
426.876.879-23 dfa
545.213.951-90 asd
138.721.165-13
'''

# print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}$', text, re.M))
text2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', text2, re.I | re.S))