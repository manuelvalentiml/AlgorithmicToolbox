s, p = [int(i) for i in input().split()]

a, b = s * [0], s * [0]
for s_ in range(s):
    tokens = [int(i) for i in input().split()]
    a[s_], b[s_] = tokens[0], tokens[1]

x = [int(i) for i in input().split()]

order = sorted(range(p), key=lambda k: x[k])
results = p * [0]

# Initialize array for solution
array = (p + 2 * s) * [[0, 0, 0]]

# Make array
for i in range(p):
    array[i] = [x[order[i]], 'p', order[i]]

for i in range(s):
    array[p + 2 * i] = [a[i], 'l', 0]
    array[p + 2 * i + 1] = [b[i], 'r', 0]

array = sorted(array, key=lambda x: (x[0], x[1]))

# Solve

for i in range(p + 2 * s):
    if array[i][1] is 'p':
        for j in range(i):
            if array[j][1] == 'l':
                results[array[i][2]] += 1
            elif array[j][1] == 'r':
                results[array[i][2]] -= 1

print(' '.join(map(str, results)))
