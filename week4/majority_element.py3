n = int(input())
a = [int(i) for i in input().split()]

res = dict()

for i in a:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

solution = 0
for i in res.values():
    if i > n // 2:
        solution = 1

print(solution)