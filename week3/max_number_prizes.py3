k = int(input())

x = int((- 1 + (1 + 8 * k) ** (1 / 2)) // 2)

results = [i+1 for i in range(x)]

results[-1] = int(k - ((x-1) + (x-1) **2) / 2)

print(len(results))
print(" ".join(map(str,results)))