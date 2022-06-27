from class1_association import *

escritor = Escritor('Jonatas')
caneta = Caneta('Baymetrics')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
