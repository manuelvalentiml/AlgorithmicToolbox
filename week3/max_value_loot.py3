def read_input(n):
    v = []
    w = []
    for i in range(n):
        tokens = input().split()

        v.append(int(tokens[0]))
        w.append(int(tokens[1]))

    return v, w


def unitary_value(v, w):
    u = []
    for i in range(len(v)):
        u.append(v[i]/w[i])
    return u


def next_item(w, u):
    i = 0
    for j in range(2, len(w)):
        if w[j] > 0 and u[j] > u[i]:
            i = j
    return i


def knapsack_naive(v, w, weight):
    n = len(w)
    a = [0] * n                     # Usage of items, between 0 and 1
    value = 0
    u = unitary_value(v, w)

    for _ in range(n):
        if weight == 0:
            return value, a
        i = next_item(w, u)
        if w[i] < weight:
            a_ = w[i]
        else:
            a_ = weight
        value += a_ * u[i]
        w[i] -= a_
        a[i] += a_
        weight -= a_

    return value, a


def pipeline(n, weight):
    v, w = read_input(n)
    value, _ = knapsack_naive(v, w, weight)
    if value % 1 > 0.49:
        value += 0.001                          # Correcting rounding issue
    return round(value, 4)


tokens = input().split()

n = int(tokens[0])
weight = int(tokens[1])

print(pipeline(n, weight))
