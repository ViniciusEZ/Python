def fat(p1=1, show=0):
    """
    :param p1: Número a ser calculado.
    :param show: Parâmetro para mostrar ou não o processo de cálculo.
    :return: Em caso de show=False, retorna apenas o resultado do fatorial.
    """
    f = 1
    if not show:
        for c in range(p1, 0, -1):
            f *= c
        return f
    else:
        for c in range(p1, 0, -1):
            print(f"{c}", end='')
            print(" x " if c > 1 else f" = {f}", end=' ')
            f *= c


user = int(input("Digite o número que deseja ver o fatorial: "))
print(fat(user, show=True))
