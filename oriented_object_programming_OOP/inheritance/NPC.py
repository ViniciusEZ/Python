class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'time: {self.time}')
        print(f'Força: {self.forca}')
        print(f'Munição: {self.municao}')
        estado = 'Sim' if self.vivo else 'Não'
        print(f'Vivo: {estado}')
        print(f'Energia: {self.energia}')
        print('-' * 30)


class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)


s1 = Guarda('Dante', 1)
s2 = Soldado('Bope', 2)
s3 = Elite('Sei lá', 2)
s4 = Guarda('Justice', 2)
s5 = Elite('Officer', 1)
s6 = Elite('Knight', 1)


s1.vivo = False

s1.info()
s2.info()
s6.info()
