num = input("Digite o primeiro número: ").split()


if int(num[0]) > int(num[1]) > int(num[2]):
    print(f"O maior número é: {num[0]}\n o menor {num[2]}")
elif int(num[0]) > int(num[2]) > int(num[1]):
    print(f"O maior número é: {num[0]}\ne o menor {num[1]}")
elif int(num[1]) > int(num[0]) > int(num[2]):
    print(f"O maior número é: {num[1]}\ne o menor {num[2]}")
elif int(num[1]) > int(num[2]) > int(num[0]):
    print(f"O maior número é: {num[1]}\ne o menor {num[0]}")
elif int(num[2]) > int(num[1]) > int(num[0]):
    print(f"O maior número é: {num[2]}\ne o menor {num[0]}")
elif int(num[2]) > int(num[0]) > int(num[1]):
    print(f"O maior número é: {num[2]}\ne o menor {num[1]}")



