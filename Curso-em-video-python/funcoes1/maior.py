from time import sleep


def maior(*num):
    maior = 0
    i = 0
    while i < len(num):
        if i == 0:
            maior = num[i]
        if num[i] > maior:
            maior = num[i]
        i += 1
    for i in num:
        print(f"{i}", end=' ')
        sleep(1)
    print(f"Foram informados {len(num)} valores.")
    print(f"O maior valor informado foi {maior}.")
    print("-=" * 20)


maior(5, 6, 1, 7, 8)
maior(10, 11, 19, 4, -1, 4)
