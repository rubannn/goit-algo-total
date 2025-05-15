import timeit
import random
from sort_functions import insertion_sort, merge_sort, timsort, merge_k_lists


def generate_test_cases(size):
    random_array = [random.randint(0, 10000) for _ in range(size)]
    sorted_array = sorted(random_array)
    reverse_sorted = sorted(random_array, reverse=True)
    partially_sorted = sorted_array[: size // 2] + [
        random.randint(0, 10000) for _ in range(size // 2)
    ]

    return {
        "random": random_array,
        "sorted": sorted_array,
        "reverse": reverse_sorted,
        "partially": partially_sorted,
    }


def measure_performance(sort_func, array):
    setup = f"from __main__ import {sort_func.__name__}; import copy; arr = copy.deepcopy({array})"
    stmt = f"{sort_func.__name__}(arr)"
    time = timeit.timeit(stmt, setup=setup, number=10) / 10
    return time


if __name__ == "__main__":
    print("Вимірювання часу виконання алгоритмів сортування:\n")

    sizes = [100, 1000, 10000]
    algorithms = [insertion_sort, merge_sort, timsort]
    case_labels = {
        "random": "Випадковий",
        "sorted": "Відсортований",
        "reverse": "У зворотному порядку",
        "partially": "Частково відсортований",
    }

    header = f"| {'Розмір':^8} | {'Тип масиву':^24} | {'insertion_sort (сек)':^20} | {'merge_sort (сек)':^20} | {'timsort (сек)':^20} |"
    row_separator = "-" * len(header)

    print(f"{row_separator}\n{header}")
    for size in sizes:
        print(row_separator)
        test_cases = generate_test_cases(size)

        for case_key, array in test_cases.items():
            row = f"| {size:^8} | {case_labels[case_key]:<24}"

            times = []
            for algorithm in algorithms:
                t = measure_performance(algorithm, array)
                times.append(f"{t:.6f}")

            row += f" | {' | '.join(f"{t:^20}" for t in times)} |"
            print(row)
    print(row_separator)

    print("\nДодаткове завдання:")
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list, "\n")
