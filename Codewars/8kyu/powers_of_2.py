def powers_of_two(n):
    list = []
    power = 1
    if n == 0:
        list.append(1)
        return list
    else:
        for i in range(0, n):
            if i == 0:
                list.append(1)
            power *= 2
            list.append(power)
        return list


print(powers_of_two(4))
