import time
import random
from quicksort import randomized_quicksort, deterministic_quicksort


def generate_random_array(size: int) -> list:
    return [random.randint(0, size) for _ in range(size)]


def generate_sorted_array(size: int) -> list:
    return list(range(size))


def generate_reverse_sorted_array(size: int) -> list:
    return list(range(size, 0, -1))


def generate_repeated_array(size: int) -> list:
    return [5] * size


def benchmark(sort_function, arr: list):
    """
    Measures execution time of a sorting function.
    Returns None if recursion limit is exceeded.
    """
    try:
        start_time = time.perf_counter()
        sort_function(arr)
        end_time = time.perf_counter()
        return end_time - start_time
    except RecursionError:
        return None


def format_time(t):
    return f"{t:.6f}s" if t is not None else "RecursionError"


def run_benchmarks():
    sizes = [1000, 3000, 5000]

    print("Benchmarking Quicksort Algorithms\n")

    for size in sizes:
        print(f"Input Size: {size}")

        datasets = {
            "Random": generate_random_array(size),
            "Sorted": generate_sorted_array(size),
            "Reverse Sorted": generate_reverse_sorted_array(size),
            "Repeated": generate_repeated_array(size)
        }

        for name, data in datasets.items():
            arr1 = data.copy()
            arr2 = data.copy()

            time_rand = benchmark(randomized_quicksort, arr1)
            time_det = benchmark(deterministic_quicksort, arr2)

            print(
                f"{name:15} | "
                f"Randomized: {format_time(time_rand):>14} | "
                f"Deterministic: {format_time(time_det)}"
            )

        print("-" * 70)


if __name__ == "__main__":
    run_benchmarks()

