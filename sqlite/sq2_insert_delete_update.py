import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    path = r"-------------------------------------------------"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as er:
        print(er)
    return con


vcon = ConexaoBanco()


# name = input("Type the name: ")
# telephone = input('Type the telephone: ')
# email = input('Type the email: ')


# vsql = f"""INSERT INTO tb_contatos
# (NameContact, T_ContactTelephone, EmailContact)
# VALUES ('{name}', '{telephone}', '{email}') """


def insert(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro inserido')
    except Error as er:
        print(er)


# insert(vcon, vsql)

def delete(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro deletado')
    except Error as er:
        print(er)


# vsql2 = '''DELETE FROM tb_contatos WHERE IDContact = 2
# '''
# delete(vcon, vsql2)

def update(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registro atualizado')
    except Error as er:
        print(er)


# vsql2 = '''UPDATE tb_contatos SET NameContact='Json', T_ContactTelephone='(11)6437984', EmailContact='J@email.com'
# WHERE IDcontact=3
# '''
# update(vcon, vsql2)

def select(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    result = c.fetchall()
    return result

vsql= 'SELECT * FROM tb_contatos WHERE NameContact LIKE "%o"'
res = select(vcon, vsql)

for r in res:
    print(r)