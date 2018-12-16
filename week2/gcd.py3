def gcd(a, b):

    if b > a:
        temp = a
        a = b
        b = temp

    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

tokens = input().split()

a = int(tokens[0])
b = int(tokens[1])

print(gcd(a, b))
