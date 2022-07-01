import re
text = """
VÁLIDAS
BKAi/i~7j;99
m^7AT_0"o8Rv
V7`1Vdnr6+~V
7ME@m3_4Hyk 
\]\hI5zTI48c

SEM MINÚSCULAS
T%Y415]>;GQ2
K72F;8N>I4''
SO<03*]3MW4~
@SS~T[08F0`1
_52C`>=9V3AJ

SEM MINÚSCULAS E NÚMEROS
:H;}TOSN&I @
($RFT(I/K^H[
`|QH=#QR^H`C
`A]TWB]<W>*D
Z]%{/IT`XWH{

SEM NÚMEROS CARACTERES E MINÚSCULAS
YAGNRXATPIXU
KYSYFHKRMFNG
MRUYBGFVJJNF
DDWQXYHMOYXN
ADGRFPENXYQS

QUANTIDADE INVÁLIDA (6)
s65q{D
l3[Na8
jA&67u
f+87Fn
K'fh33
"""

regex = re.compile(r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[ -\/:-@[-`{-~]+).{12,}', re.M)
print(regex.findall(text))