list = []
for i in range(0, 5):
    user = int(input("Digite um número: "))
    if i == 0 or user > (list[-1]):
        print("Inserido no fim da lista")
        list.append(user)
    else:
        for c in range(0, len(list)):
            if user < list[c]:
                print(f"Inserido na {c} posição")
                list.insert(c, user)
                break
            c += 1

print(list)