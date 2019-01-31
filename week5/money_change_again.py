# Uses python3
import sys

COINS = [1, 3, 4]


def get_change(n):

    # Assuming the first coin is 1
    values = [0] * (n+1)

    for i in range(1, n+1):
        values[i] = values[i-1] + 1
        for coin in COINS[1:]:
            if coin <= i:
                values[i] = min(values[i], values[i-coin] + 1)
    return values[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
