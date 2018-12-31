import random


def partition3(array, left, right):
    value = array[left]
    low = left
    high = right
    i = left
    while i <= high:
        if value > array[i]:
            array[i], array[low] = array[low], array[i]
            low += 1
            i += 1
        elif value < array[i]:
            array[i], array[high] = array[high], array[i]
            high -= 1
        else:
            i += 1
    return low, high


def partition2(array, left, right):
    value = array[left]
    position = left
    for i in range(left + 1, right + 1):
        if array[i] <= value:
            position += 1
            array[i], array[position] = array[position], array[i]
    array[left], array[position] = array[position], array[left]
    return position


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    array[left], array[k] = array[k], array[left]
    #use partition3
    l,r = partition3(array, left, right)
    randomized_quick_sort(array, left, l - 1);
    randomized_quick_sort(array, r + 1, right);


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    randomized_quick_sort(a, 0, n - 1)
    print(' '.join(map(str, a)))
