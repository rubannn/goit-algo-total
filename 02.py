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

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_result.append(val)

        # Якщо є наступний елемент у поточному списку, додаємо його до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return merged_result


data = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Об'єднаний відсортований список:", merge_k_lists(data))
