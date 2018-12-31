def read_input():
    tokens = [int(i) for i in input().split()]
    int_, list_ = tokens[0], tokens[1: tokens[0] + 1]
    return int_, list_


def binary_search_recursive(key, sorted_list, start, end):
    mid = (start + end) // 2
    if start > end:
        return -1
    elif key == sorted_list[mid]:
        return mid
    elif key < sorted_list[mid]:
        return binary_search_recursive(key, sorted_list, start=start, end=mid - 1)
    else:
        return binary_search_recursive(key, sorted_list, start=mid + 1, end=end)


def binary_search(key, sorted_list):
    return binary_search_recursive(key, sorted_list, start=0, end=len(sorted_list) - 1)


n, a = read_input()
k, b = read_input()

results = []

for i in b:
    results.append(binary_search(i, a))

print(' '.join(map(str, results)))

