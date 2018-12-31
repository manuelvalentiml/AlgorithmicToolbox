def merge_sort(a, verbose=False):
    global inversions
    if verbose:
        print("Splitting ", a)
    if len(a) > 1:
        mid = len(a) // 2

        left = a[:mid]
        right = a[mid:]

        merge_sort(left, verbose)
        merge_sort(right, verbose)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
                # Add a number of inversions equal to the number of remaining elements from 'left' when an element from
                # 'right in placed into list a
                inversions += len(left) - i
                if verbose:
                    print('Inversion!')
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    if verbose:
        print("Merging ", a)


def run():
    n = int(input())
    a = [int(x) for x in input().split()]

    global inversions
    inversions = 0
    merge_sort(a)
    print(inversions)


run()
