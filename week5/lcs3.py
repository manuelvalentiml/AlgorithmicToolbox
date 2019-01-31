# Uses python3


def lcs2(sequence1, sequence2, sequence3):

    sequence1 = [0] + sequence1
    sequence2 = [0] + sequence2
    sequence3 = [0] + sequence3

    n1 = len(sequence1)
    n2 = len(sequence2)
    n3 = len(sequence3)

    d = [[[0 for _ in range(n3)] for _ in range(n2)] for _ in range(n1)]

    for x in range(1, n1):
        for y in range(1, n2):
            for z in range(1, n3):
                if (sequence1[x] == sequence2[y]) and (sequence2[y] == sequence3[z]):
                    match_mismatch = d[x-1][y-1][z-1] + 1
                else:
                    match_mismatch = d[x-1][y-1][z-1]
                insertion_x = d[x - 1][y][z]
                insertion_y = d[x][y - 1][z]
                insertion_z = d[x][y][z - 1]

                d[x][y][z] = max(insertion_x, insertion_y, insertion_z, match_mismatch)

    return d[-1][-1][-1]


_ = int(input())
seq1 = [int(i) for i in input().split()]
_ = int(input())
seq2 = [int(i) for i in input().split()]
_ = int(input())
seq3 = [int(i) for i in input().split()]

print(lcs2(seq1, seq2, seq3))
