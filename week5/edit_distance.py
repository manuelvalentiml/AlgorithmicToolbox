# Uses python3
def edit_distance(word1, word2):

    word1 = '-' + word1
    word2 = '-' + word2

    n1 = len(word1)
    n2 = len(word2)

    d = [[0 for _ in range(n2)] for _ in range(n1)]

    for i in range(n1):
        d[i][0] = i

    for i in range(n2):
        d[0][i] = i

    for x in range(1, n1):
        for y in range(1, n2):
            if word1[x] == word2[y]:
                match_mismatch = d[x-1][y-1]
            else:
                match_mismatch = d[x-1][y-1] + 1
            insertion = d[x - 1][y] + 1
            deletion = d[x][y - 1] + 1

            d[x][y] = min(insertion, deletion, match_mismatch)
    return d[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
