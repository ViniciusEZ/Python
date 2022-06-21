from random import randint
c = 0

while True:
    user = input("Par ou ímpar? [P/I]: ").upper()
    print("=========================")
    user1 = int(input("Digite um valor: "))
    print("=========================")
    mac = randint(0, 10)
    s = user1 + mac
    if user == "P":
        if s % 2 == 0:
            print(f"Você jogou {user1} e a máquina {mac}. O total deu {s}")
            print("Você ganhou!")
            c += 1
        else:
            print(f"Você jogou {user1} e a máquina {mac}. O total deu {s}")
            print("Você perdeu!")
            break
    elif user == "I":
        if s % 2 == 1:
            print(f"Você jogou {user1} e a máquina {mac}. O total deu {s}")
            print("Você ganhou!")
            c += 1
        else:
            print(f"Você jogou {user1} e a máquina {mac}. O total deu {s}")
            print("Você perdeu!")
            break


print(f"\nVocê ganhou {c} partidas!")







