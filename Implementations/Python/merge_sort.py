"""Merge sort using an auxiliary copy of each pair of sorted halves."""


def merge(values, left, middle, right):
    """Merge sorted inclusive ranges values[left:middle+1] and values[middle+1:right+1]."""
    left_part = values[left:middle + 1]
    right_part = values[middle + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        # Taking from the left on equality preserves stability.
        if left_part[i] <= right_part[j]:
            values[k] = left_part[i]
            i += 1
        else:
            values[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        values[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        values[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(values, left=0, right=None):
    """Sort values in place in nondecreasing order and return the same list."""
    if right is None:
        right = len(values) - 1
    if left >= right:
        return values

    middle = (left + right) // 2
    merge_sort(values, left, middle)
    merge_sort(values, middle + 1, right)
    merge(values, left, middle, right)
    return values


if __name__ == "__main__":
    sample = [3, 41, 52, 26, 38, 57, 9, 49]
    print(merge_sort(sample))
