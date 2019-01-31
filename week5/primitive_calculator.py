# Uses python3
import sys

MULTIPLICATIONS = [2, 3]


def count_operatiosn(n):

    # Assuming the first coin is 1
    values = [0] * (n+1)
    operations = [0] * (n+1)

    for i in range(2, n+1):
        values[i] = values[i-1] + 1
        for mult in MULTIPLICATIONS:
            if i % mult == 0:
                test_value = values[i // mult] + 1
                if test_value < values[i]:
                    operations[i] = mult
                    values[i] = test_value

    output = [n]
    i = n
    while i > 1:
        if operations[i] == 0:
            i -= 1
        else:
            i = i // operations[i]

        output = [i] + output

    return values[-1], output


if __name__ == '__main__':
    m = int(sys.stdin.read())
    v, o = count_operatiosn(m)
    print(str(v) + '\n' + ' '.join(map(str, o)))

