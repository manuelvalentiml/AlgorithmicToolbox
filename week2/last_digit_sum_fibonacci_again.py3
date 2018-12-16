def fibonacci_fast(n):
    if n <= 1:
        return n
    else:
        a = [0, 1]
        for i in range(1, n):
            a.append(a[-1] + a[-2])
        return a[-1]


def last_digit_fibonacci_sum_period():
    sequence = [0, 1]
    for period in range(2, 101):
        sequence.append((sequence[-1] + fibonacci_fast(period)) % 10)
        if sequence[-2] == 0 and sequence[-1] == 1:
            return sequence[:-2], period-1


def last_digit_fibonacci_sum(n):
    sequence, period = last_digit_fibonacci_sum_period()
    return sequence[n % period]


def last_digit_fibonacci_sum_again(n, m):
    return (10 + last_digit_fibonacci_sum(m) - last_digit_fibonacci_sum(n - 1)) % 10


tokens = input().split()

n = int(tokens[0])
m = int(tokens[1])

print(last_digit_fibonacci_sum_again(n, m))
