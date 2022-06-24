from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criarArquivo(arq)



while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

