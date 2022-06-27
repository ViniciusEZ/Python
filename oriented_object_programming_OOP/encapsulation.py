# _ protected (public _)
# __ private (_NAMECLASS__ATRIBUTNAME)
class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1, 'Vinicius')
bd.inserir_cliente(2, 'Jason')
bd.inserir_cliente(3, 'Beato')
print(bd.dados)
#bd.__dados = 'Alguma coisa'
# print(bd.__dados)
#print(bd._BaseDeDados__dados)
#bd.lista_clientes()
