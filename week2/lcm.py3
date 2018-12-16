def gcd(a, b):

    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


tokens = input().split()

a = int(tokens[0])
b = int(tokens[1])

print(lcm(a, b))
