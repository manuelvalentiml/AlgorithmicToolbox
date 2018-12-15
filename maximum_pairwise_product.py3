def max_pairwise_product_naive(a):
    product = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            product = max(product, a[i] * a[j])
    return(product)


def max_pairwise_product_fast(n, a):
    index_1 = 0
    for i in range(1, n):
        if a[i] > a[index_1]:
            index_1 = i
    if index_1 == 0:
        index_2 = 1
    else:
        index_2 = 0
    for i in range(index_2 + 1, n):
        if a[i] > a[index_2] and i != index_1:
            index_2 = i
    return a[index_1] * a[index_2]


n = int(input())
a = [int(x) for x in input().split()]

print(max_pairwise_product_fast(n, a))