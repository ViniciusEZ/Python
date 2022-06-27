from class_single_inheritance import *

"""
Associação - Usa / Agregação - Tem / Composição - É dono / Herança - Filha
"""

c1 = Cliente('Vinicius', 18)
print(c1.idade)
c1.falar()
c1.comprar()
print()
a1 = Aluno('Viktor', 20)
print(a1.nome)
a1.falar()
a1.estudar()