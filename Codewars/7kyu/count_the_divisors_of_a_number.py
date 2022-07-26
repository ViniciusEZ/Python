# Count the number of divisors of a positive integer n.

def divisors(n):
    return len([x for x in range(1, n+1) if n % x == 0])


print(divisors(4))