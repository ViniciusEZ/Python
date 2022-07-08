# Create function fib that returns n'th element of Fibonacci sequence
def fibonacci(n: int) -> int:
        t1 = 0
        t2 = 1
        c = 0
        t3 = 0
        if n == 1:
            return 1
        while c < n-1:
            t3 = t1 + t2
            t1 = t2
            t2 = t3
            c += 1
        return t3

print(fibonacci(2))