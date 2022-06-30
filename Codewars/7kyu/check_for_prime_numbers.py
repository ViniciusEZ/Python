def is_prime(n):
    m = 0
    for i in range(1, n):
        if n % i == 0:
            m += 1
    return m == 1


print(is_prime(11))
