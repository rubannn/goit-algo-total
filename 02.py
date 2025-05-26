import heapq


def merge_k_lists(lists):
    if not lists:
        return []

    min_heap = []
    merged_result = []

    # Додаємо перший елемент кожного списку у купу разом з індексами
    for i, lst in enumerate(lists):
        if lst:  # Якщо список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))

    # Поки купа не порожня, витягуємо найменший елемент
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_result.append(val)

        # Якщо є наступний елемент у поточному списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))


    return merged_result


data = [
    ([1, 4, 5], [1, 3, 4], [2, 6]),
    ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [0, 10, 20, 30]),
    ([-5, -3, 0, 2, 4], [1, 2, 3, 4, 5], [10, 20, 30], [-10, -8, -6]),
    ([7, 14, 21, 28], [3, 6, 9, 12], [0, 1, 1, 2, 3, 5, 8]),
    ([-20, -15, -10, -5, 0], [5, 10, 15, 20], [100, 200], [0, 0, 0, 1, 1]),
]

for i, test in enumerate(data):
    print(f"\nНабір даних {i + 1}:")
    for lst in test:
        print(lst)
    print("Об'єднаний відсортований список:", merge_k_lists(test))

