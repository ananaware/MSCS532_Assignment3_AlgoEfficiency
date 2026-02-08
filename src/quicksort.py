import random
from typing import List


# =========================
# Randomized Quicksort
# =========================

def randomized_quicksort(arr: List[int]) -> None:
    """
    Sorts the list in-place using Randomized Quicksort.
    """
    if arr is None or len(arr) <= 1:
        return
    _randomized_quicksort(arr, 0, len(arr) - 1)


def _randomized_quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _randomized_partition(arr, low, high)
        _randomized_quicksort(arr, low, pivot_index - 1)
        _randomized_quicksort(arr, pivot_index + 1, high)


def _randomized_partition(arr: List[int], low: int, high: int) -> int:
    """
    Chooses a random pivot uniformly at random and partitions the array.
    """
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    return _partition(arr, low, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto partition scheme.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# =========================
# Deterministic Quicksort
# (First element as pivot)
# =========================

def deterministic_quicksort(arr: List[int]) -> None:
    """
    Deterministic Quicksort using the first element as pivot.
    """
    if arr is None or len(arr) <= 1:
        return
    _deterministic_quicksort(arr, 0, len(arr) - 1)


def _deterministic_quicksort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _deterministic_partition(arr, low, high)
        _deterministic_quicksort(arr, low, pivot_index - 1)
        _deterministic_quicksort(arr, pivot_index + 1, high)


def _deterministic_partition(arr: List[int], low: int, high: int) -> int:
    """
    Uses the first element as pivot.
    """
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


# =========================
# Manual Testing
# =========================

if __name__ == "__main__":
    test_arrays = [
        [],
        [1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 3, 3, 3],
        [5, 1, 4, 2, 8, 5, 3]
    ]

    print("Randomized Quicksort:")
    for arr in test_arrays:
        a = arr.copy()
        randomized_quicksort(a)
        print(a)

    print("\nDeterministic Quicksort:")
    for arr in test_arrays:
        a = arr.copy()
        deterministic_quicksort(a)
        print(a)

