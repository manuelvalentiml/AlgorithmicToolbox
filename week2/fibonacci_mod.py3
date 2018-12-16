def fibonacci_fast(n):
    if n <= 1:
        return n
    else:
        a = [0, 1]
        for i in range(1, n):
            a.append(a[-1] + a[-2])
        return a[-1]


def fibonacci_period(b):
    for i in range(1, b * b + 1):
        if fibonacci_fast(i) % b == 0 and fibonacci_fast(i+1) % b == 1:
            return(i)


def pisano_period(base):

    sequence = []
    period = fibonacci_period(base)
    for i in range(period):
        sequence.append(fibonacci_fast(i) % base)

    return sequence, period


def fibonacci_mod(n, m):
    period = fibonacci_period(m)
    return fibonacci_fast(n % period) % m


tokens = input().split()

n = int(tokens[0])
m = int(tokens[1])

print(fibonacci_mod(n, m))