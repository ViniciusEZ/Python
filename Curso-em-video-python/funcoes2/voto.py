def voto(p1):
    from datetime import datetime
    ida = datetime.now().year - user
    if ida < 16:
        return f"Com {ida} anos. Não vota!"
    elif 16 <= ida <= 18 or ida > 65:
        return f"Com {ida} anos. Voto opcional!"
    else:
        return f"Com {ida} anos. Voto obrigatório!"


user = int(input("Em que ano você nasceu? "))
print(voto(user))

