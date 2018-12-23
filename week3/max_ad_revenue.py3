def int_vector_input():
    tokens = input().split()
    for i in range(len(tokens)):
        tokens[i] = int(tokens[i])

    return tokens


def naive_sort(v):
    n = len(v)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if v[j] < v[i]:
                min_index = j
        v[i], v[min_index] = v[min_index], v[i]

    return v


def max_revenue(a, b):

    revenue = sum([a[i] * b[i] for i in range(len(a))])

    return revenue


n = int(input())
a = [int(i) for i in input().split()].sort()
b = [int(i) for i in input().split()].sort()
print(sum([a[i] * b[i] for i in range(len(a))]))
