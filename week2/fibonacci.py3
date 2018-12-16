def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)


def fibonacci_fast(n):
    if n <= 1:
        return n
    else:
        a = [0, 1]
        for i in range(1, n):
            a.append(a[-1] + a[-2])
        return a[-1]


n = int(input())
print(fibonacci_fast(n))
