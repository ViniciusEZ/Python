pri = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
decimo = pri + (10 - 1) * r
for i in range(pri, decimo + r, r):
    print(f"->{i} ")

