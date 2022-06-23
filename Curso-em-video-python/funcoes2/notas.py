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
    return nota



resp = notas(1, 2, 3, 4)
print(resp)
