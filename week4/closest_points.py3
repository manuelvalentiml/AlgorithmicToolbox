import sys
import math


def distance_squared(a, b):
    return math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2)


def distance_naive(points, d=10**18):

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            d_new = distance_squared(points[i], points[j])
            if d_new < d:
                d = d_new
    return d


def get_input():
    input = sys.stdin.read()
    # input = '12 4 4 -2 -2 -3 -4 -1 3 2 3 -4 0 1 1 -1 -1 3 -1 -4 2 -2 4'
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])

    return points_sorted_x, points_sorted_y, n


def distance_recursive(points_sorted_x, points_sorted_y, n):

    if n <= 3:
        return distance_naive(points_sorted_x)

    mid = n // 2

    x_left, x_right = points_sorted_x[:mid], points_sorted_x[mid:]
    y_left, y_right = list(), list()  # points_sorted_y[:mid], points_sorted_y[mid:]

    set_x_left = set(x_left)
    for point in points_sorted_y:
        if point in set_x_left:
            y_left.append(point)
        else:
            y_right.append(point)

    d_left = distance_recursive(x_left, y_left, mid)
    d_right = distance_recursive(x_right, y_right, n-mid)

    d = min(d_left, d_right)

    # Filter points

    line_x = points_sorted_x[mid][0]

    points_in_strip = [p for p in set(points_sorted_y) if abs(line_x - p[0]) <= d]

    n_strip = len(points_in_strip)
    for i in range(n_strip - 1):
        for j in range(i + 1, min(i + 7, n_strip)):
            d_new = distance_squared(points_in_strip[i], points_in_strip[j])
            if d_new < d:
                d = d_new
    return d


if __name__ == '__main__':
    points_x, points_y, n_ = get_input()
    print("{0:.9f}".format(math.sqrt(distance_recursive(points_x, points_y, n_))))
