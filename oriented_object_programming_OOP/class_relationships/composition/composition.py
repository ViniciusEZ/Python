cliente1 = Cliente('Vinicius', 18)
cliente1.insere_endereco('Caieiras', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Gabriel', 30)
cliente2.insere_endereco('Rio Branco', 'AC')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Maria', 50)
cliente3.insere_endereco('Salvador', 'BA')
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

