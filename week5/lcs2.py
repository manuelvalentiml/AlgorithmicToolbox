# Uses python3


def lcs2(sequence1, sequence2):

    sequence1 = [0] + sequence1
    sequence2 = [0] + sequence2

    n1 = len(sequence1)
    n2 = len(sequence2)

    d = [[0 for _ in range(n2)] for _ in range(n1)]

    for i in range(n1):
        d[i][0] = 0

    for i in range(n2):
        d[0][i] = 0

    for x in range(1, n1):
        for y in range(1, n2):
            if sequence1[x] == sequence2[y]:
                match_mismatch = d[x-1][y-1] + 1
            else:
                match_mismatch = d[x-1][y-1]
            insertion = d[x - 1][y]
            deletion = d[x][y - 1]

            d[x][y] = max(insertion, deletion, match_mismatch)

    return d[-1][-1]


n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
b = [int(i) for i in input().split()]

print(lcs2(a, b))
