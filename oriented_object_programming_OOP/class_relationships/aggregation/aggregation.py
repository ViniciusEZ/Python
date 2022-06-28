from class2_aggregation import *

carrinho = CarrinhoDeCompras()

p1 = Produto('iPhone', 10000)
p2 = Produto('Caneca', 10)
p3 = Produto('Camiseta', 20)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p1)

carrinho.lista_produto()
print(carrinho.soma_total())
