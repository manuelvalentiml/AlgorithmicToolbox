
def argmin(x):

    min = x[0]
    arg = 0
    for i in range(1, len(x)):
        if x[i] < min:
            min = x[i]
            arg = i

    return arg, min


# Read data
n = int(input())
a, b = [0]*n, [0]*n

segments = []

for i in range(len(a)):
    a[i], b[i] = [int(x) for x in input().split()]

while len(a) != 0:

    idx, _ = argmin(a)
    segments.append(b[idx])
    for i in range(len(a)):
        if b[i] < segments[-1] and b[i] < b[idx]:
            segments[-1] = b[i]
    for i in reversed(range(len(a))):
        if a[i] <= segments[-1] <= b[i]:
            a.pop(i)
            b.pop(i)

print(len(segments))
print(' '.join(map(str, segments)))
