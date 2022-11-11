def sort_with_replacement(arr: list) -> list:
    """ сортировка обeменами """
    # O(n^2)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def quick_sort(arr: list) -> list:
    """ быстрая сортировка """
    # O(n * log n)

    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2
    mid = arr[mid_idx]
    left = []
    right = []

    for idx, val in enumerate(arr):
        if idx == mid_idx:
            continue

        if val < mid:
            left.append(val)
        else:
            right.append(val)

    return [
        *quick_sort(left),
        mid,
        *quick_sort(right)
    ]


def merge_sort(arr: list) -> list:
    """ сортировка слиянием """
    # O(n * log n)

    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2
    left = merge_sort(arr[:mid_idx])
    right = merge_sort(arr[mid_idx:])
    res = []

    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    return left + res + right


def sieve_of_eratosthenes(n):
    """ решето эратосфена """
    # O(n * log n)

    resp = [True] * (n + 1)
    resp[0] = resp[1] = True

    for i in range(2, n + 1):
        for j in range(i, n // i + 1):
            x = i * j
            resp[x] = False

    return resp


print(sort_with_replacement([2, 7, 7, 2, 0, 8, 1, 9]))
print(quick_sort([2, 7, 7, 2, 0, 8, 1, 9]))
print(merge_sort([2, 7, 7, 2, 0, 8, 1, 9]))
print(sieve_of_eratosthenes(20))
