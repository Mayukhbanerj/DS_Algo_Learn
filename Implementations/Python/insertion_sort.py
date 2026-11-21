"""Insertion sort, translated to Python's zero-based indexing."""


def insertion_sort(values):
    """Sort values in place in nondecreasing order and return the same list.

    The strict comparison preserves the relative order of equal keys, so this
    implementation is stable.
    """
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values


if __name__ == "__main__":
    sample = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(sample))
