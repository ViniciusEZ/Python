import sqlite3
from sqlite3 import Error


# Criando conexão
def ConexaoBanco():
    path = r"-----------------------------------------------------"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as er:
        print(er)
    return con


vcon = ConexaoBanco()

# Create table
vsql = '''CREATE TABLE tb_contatos(
          IDContact integer primary key autoincrement,
          NameContact varchar(30),
          T_ContactTelephone varchar(14),
          EmailContact varchar(30)
);
'''


def CreateTable(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as er:
        print(er)


CreateTable(vcon, vsql)
vcon.close()
