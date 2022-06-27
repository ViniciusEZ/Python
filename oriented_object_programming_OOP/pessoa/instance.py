from pessoa import Pessoa

p1 = Pessoa('Vinicius', 29)
p2 = Pessoa('João', 32)
p3 = Pessoa.por_ano_nascimento('Luiz', 1978)
print(p3.nome, p3.idade)

p1.comer('churrasco')
p2.falar('jogos')
p1.falar('moto')
print(Pessoa.gera_id())
