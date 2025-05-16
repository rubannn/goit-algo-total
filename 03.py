# Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі
# двох текстових файлів (стаття 1, стаття 2 (\in)). Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох
# видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням).
# На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.

# Зроблено висновки щодо швидкостей алгоритмів для кожного тексту окремо та в цілому.
# Висновки оформлено у вигляді документа формату markdown.


import os
import timeit
from algo_txt_search import rabin_karp_search, boyer_moore_search, kmp_search

# Каталог із вхідними файлами
input_dir = "in"

# Цільові підрядки для пошуку
targets = [
    {"exist": "цільовий елемент", "fake": "неіснуючий елемент"},
    {"exist": "формування рекомендацій", "fake": "griph database"},
]

# Отримуємо всі .txt файли з каталогу
txt_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

header = f"| {'Файл':^20} | {'Тип':^10} | {'Рядок':^25} | {'KMP пошук (сек)':^20} | {'Rabin-Karp пошук (сек)':^30} | {'Boyer-Moore пошук (сек)':^30} |"
row_separator = "-" * len(header)

# Вивід шапки таблиці
print(f"{row_separator}\n{header}\n{row_separator}")

# Проходимося по кожному файлу
for num, filename in enumerate(txt_files):
    file_path = os.path.join(input_dir, filename)
    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    # Проходимося по кожному набору цільових підрядків
    for key, substring in targets[num].items():
        # Вимірюємо час роботи алгоритму KMP
        kmp_time = timeit.timeit(lambda: kmp_search(text, substring), number=1)

        # Вимірюємо час роботи алгоритму Рабіна-Карпа
        rk_time = timeit.timeit(lambda: rabin_karp_search(text, substring), number=1)

        # Вимірюємо час роботи алгоритму Бойєра-Мура
        bm_time = timeit.timeit(lambda: boyer_moore_search(text, substring), number=1)

        # Вивід результатів у вигляді рядка таблиці
        print(
            f"| {filename:^20} | {key:^10} | {substring:^25} | {kmp_time:^20.6f} | {rk_time:^30.6f} | {bm_time:^30.6f} |"
        )
    print(f"{row_separator}")
