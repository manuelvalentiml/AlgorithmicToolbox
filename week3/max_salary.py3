n = int(input())
x = [int(i) for i in input().split()]


def is_greater_or_equal(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(x):
    answer = []

    while x:
        max_digit = 0
        for digit in x:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        x.remove(max_digit)

    return answer


print(''.join([str(i) for i in largest_number(x)]))
