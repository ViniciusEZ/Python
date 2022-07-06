import os
import sqlite3
from sqlite3 import Error


# Connection

def DBConnection():
    path = r"-----------------------------------------"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as er:
        print(er)
    return con


vcon = DBConnection()


def query(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Operação realizada com sucesso')
    except Error as er:
        print(f"{er}")
    finally:
        pass
        # connection.close()


def select(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    res = c.fetchall()
    # connection.close()
    return res


def menuP():
    os.system("cls")
    print('1 - Inserir novo registro')
    print('2 - Deletar registro')
    print('3 - Atualizar registro')
    print('4 - Consultar registros')
    print('5 - Consultar registro por nome')
    print('6 - Sair')


def insert():
    os.system("cls")
    name = input('Digite o nome: ')
    telephone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    vsql = f"INSERT INTO tb_contatos (NameContact, T_ContactTelephone, EmailContact) VALUES ('{name}', '{telephone}', '{email}')"
    query(vcon, vsql)


def delete():
    os.system("cls")
    id = int(input("Digite o ID do registro a ser deletado: "))
    vsql = f"DELETE FROM tb_contatos WHERE IDContact={id}"
    query(vcon, vsql)


def update():
    os.system("cls")
    vid = int(input("Digite o ID do registro a ser alterado: "))
    r = select(vcon, f"SELECT * FROM tb_contatos WHERE IDContact={vid}")
    rname = r[0][1]
    rtelephone = r[0][2]
    remail = r[0][3]
    vname = input("Digite o nome: ")
    vtelephone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    if len(vname) == 0:
        vname = rname
    if len(vtelephone) == 0:
        vtelephone = rtelephone
    if len(vemail) == 0:
        vemail = remail
    vsql = f"UPDATE tb_contatos SET NameContact='{vname}', T_ContactTelephone='{vtelephone}', EmailContact='{vemail}' WHERE IDContact={vid}"
    query(vcon, vsql)


def selecty():
    vsql = "SELECT * FROM tb_contatos"
    res = select(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"ID: {r[0]:_<3} Nome: {r[1]:_<10} Telefone: {r[2]:_<15} Email: {r[3]}")
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system("cls")
    print("Fim da lista")


def selectName():
    vname = input("Digite o nome: ")
    vsql = f"SELECT * FROM tb_contatos WHERE NameContact LIKE '%{vname}%'"
    res = select(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"ID: {r[0]:_<3} Nome: {r[1]:_<10} Telefone: {r[2]:_<15} Email: {r[3]}")
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system("cls")


op = 0
while op != 6:
    menuP()
    op = int(input('Digite uma opção: '))
    if op == 1:
        insert()
    elif op == 2:
        delete()
    elif op == 3:
        update()
    elif op == 4:
        selecty()
    elif op == 5:
        selectName()
    elif op == 6:
        os.system("pause")
        print("Programa finalizado...")
    else:
        os.system("cls")
        print('Opção inválida')
        os.system("pause")

vcon.close()
os.system("pause")
