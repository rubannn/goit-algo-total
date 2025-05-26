import heapq
import random


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


def generate_test_data(
    num_datasets=5,
    max_lists_per_dataset=4,
    max_elements_per_list=7,
    min_value=-20,
    max_value=30,
):
    data = []
    for _ in range(num_datasets):
        num_lists = random.randint(2, max_lists_per_dataset)
        dataset = []
        for _ in range(num_lists):
            num_elements = random.randint(2, max_elements_per_list)
            lst = sorted(
                [random.randint(min_value, max_value) for _ in range(num_elements)]
            )
            dataset.append(lst)
        data.append(dataset)
    return data


# Генеруємо тестові дані
data = generate_test_data(max_elements_per_list=5)

# Виводимо результати для кожного набору даних
for i, test in enumerate(data):
    print(f"\nНабір даних {i + 1}:")
    for lst in test:
        print(lst)
    print("Об'єднаний відсортований список:", merge_k_lists(test))
