def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def timsort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = [the_array[0]]

    # для кожного i в діапазоні від 1 до довжини масиву
    for i in range(1, length):
        # якщо i знаходиться в кінці списку
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        # якщо i-й елемент масиву менший за попередній
        if the_array[i] < the_array[i - 1]:
            # якщо new_run не ініціалізовано (NULL)
            if not new_run:
                runs.append([the_array[i]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        # інакше, якщо він дорівнює або більший
        else:
            new_run.append(the_array[i])

    # для кожного елемента в runs, додайте його за допомогою сортування вставками
    for item in runs:
        sorted_runs.append(insertion_sort(item))

    # для кожного run у sorted_runs, об'єднайте їх
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array


def merge_k_lists(lists):
    if not lists:
        return []

    # Поки є більше одного списку, об'єднуйте їх попарно
    while len(lists) > 1:
        merged_lists = []

        # Об'єднуємо списки попарно
        for i in range(0, len(lists), 2):
            left = lists[i]
            right = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge(left, right))

        lists = merged_lists

    return lists[0]

