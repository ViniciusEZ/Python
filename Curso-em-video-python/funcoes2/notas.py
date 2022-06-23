def notas(*num, sit=0):
    nota = {}
    s = maior = menor = total = 0
    for i in range(0, len(num)):
        if i == 0:
            maior = menor = num[i]
        else:
            if num[i] > maior:
                maior = num[i]
            nota['Maior'] = maior
            if num[i] < menor:
                menor = num[i]
                nota['Menor'] = menor
        total += 1
        nota['Total'] = total
    for n in num:
        s += n
    nota['Média'] = s / total
    if sit:
        if nota['Média'] <= 6:
            nota['Situação'] = "Ruim"
        else:
            nota['Situação'] = "Boa"
    return nota


resp = notas(10,7, 9,10, 1, 6, 6,sit=True)
print(resp)
