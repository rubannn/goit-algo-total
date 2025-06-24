# Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами.
# Написана функція для двійкового пошуку повинна повертати кортеж, де першим
# елементом є кількість ітерацій, потрібних для знаходження елемента. Другим
# елементом має бути "верхня межа" — це найменший елемент, який є більшим
# або рівним заданому значенню.
import random


def gen_sorted_float_array(size, min_val=0.0, max_val=100.0):
    """Генерує відсортований масив випадкових дробових чисел."""
    arr = [round(random.uniform(min_val, max_val), 3) for _ in range(size)]
    arr.sort()  # Сортуємо масив
    return arr


def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо upper_bound не знайдено (тобто всі елементи менші за target)
    if upper_bound is None and len(arr) > 0:
        upper_bound = arr[-1]  # Останній елемент - найбільший у відсортованому масиві

    return (iterations, upper_bound)


arr = gen_sorted_float_array(20)  # Генеруємо масив з 10 чисел
target = round(random.uniform(0.0, 100.0), 3)  # Випадкове цільове значення

print("Згенерований масив:", arr)
print("Шукане значення:", target)

result = bin_search(arr, target)
print("Результат пошуку (ітерації, верхня межа):", result)
