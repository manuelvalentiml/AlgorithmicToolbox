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


def fibonacci_sequence():

    sequence = []
    period = fibonacci_period(10)
    for i in range(period):
        sequence.append(fibonacci_fast(i) % 10)

    return sequence, period


def last_digit_fibonacci_naive(n):
    return fibonacci_fast(n) % 10


def last_digit_fibonacci_fast1(n):
    if n <= 1:
        return n
    else:
        a = [0, 1]
        for i in range(1, n):
            a[0] = a[1]
            a[1] = (a[-1] + a[-2]) % 10
        return a[1]


def last_digit_fibonacci_fast2(n):

    sequence, period = fibonacci_sequence()

    return sequence[n % period]


n = int(input())
print(last_digit_fibonacci_fast2(n))