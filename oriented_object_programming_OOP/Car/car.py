class Car:
    def __init__(self, nomeC, velM, cor, ligado= False):
        self.nomeC = nomeC
        self.velM = velM
        self.cor = cor
        self.ligado = ligado

    def show(self):
        print(f'Nome do carro: {self.nomeC}')
        print(f'Velocidade máxima: {self.velM}')
        print(f'Cor: {self.cor}')
        estado = 'Sim' if self.ligado else 'Não'
        print(f'Ligado: {estado}')
        print('-'*30)

    def ligar(self):
        if self.ligado:
            print('O carro já está ligado!')
            return
        print('Ligando o carro...')
        self.ligado = True

    def desligar(self):
        if self.ligado:
            print('Desligando o carro')
            self.ligado = False
            return
        print('O carro já está desligado!')

    def andar(self):
        if self.ligado:
            print('Carro andando...')
            return
        print('Carro está desligado!')



