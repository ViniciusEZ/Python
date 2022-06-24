def metade(preco=0, formatar=0):
    n = preco / 2
    if format:
        return moeda(n)
    else:
        return n


def dobro(preco=0, formatar=0):
    n = preco * 2
    if format:
        return moeda(n)
    else:
        return n


def aumentar(preco=0, taxa=0, formatar=0):
    n = preco + (preco * (taxa / 100))
    if format:
        return moeda(n)
    else:
        return n


def diminuir(preco=0, taxa=0, formatar=0):
    n = preco - (preco * (taxa / 100))
    if format:
        return moeda(n)
    else:
        return n


def moeda(preco=0, moeda='R$'):
    return f"{moeda}{preco:.2f}".replace('.', ',')


def resumo(preco=0, aumento=0, dim=0):
    print('-'*25)
    print("RESUMO DO VALOR")
    print('-'*25)
    print(f"Preço analisado: \t{moeda(preco)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{metade(preco, True)}")
    if aumento:
        print(f"{aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    if diminuir:
        print(f"{dim}% de redução: \t{diminuir(preco, dim, True)}")
    print('-'*25)