times = (
'São Paulo', 'Corinthians', 'Palmeiras', 'Internacional', 'Atlético-MG', 'Atlético-PR', 'Botafogo', 'Fluminense',
'Flamengo', 'Bahia', 'Chapecoense', 'Santos', 'Vasco', 'Grêmio', 'Fortaleza', 'Remo', 'Coritiba', 'Sport', 'Cruzeiro',
'Bragantino')

print(f"Os 5 primeiro colocados são: {times[0:5]}")
print(f"Os 4 últimos da são: {times[-4:]}")
print(f"Os times em ordem alfabética: {sorted(times)}")
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}º posição')
