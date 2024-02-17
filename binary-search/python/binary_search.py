def binary_search(tgt, lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == tgt:
            return mid
        elif lst[mid] > tgt:
            right = mid - 1
        else:
            left = mid + 1
    return -1