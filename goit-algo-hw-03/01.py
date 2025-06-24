# 1. Парсинг аргументів. Скрипт приймає два аргументи командного рядка: шлях до вихідної директорії та шлях до
# директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).

# 2. Рекурсивне читання директорій:
# Написана функція, яка приймає шлях до директорії як аргумент.
# Функція перебирає всі елементи у директорії.
# Якщо елемент є директорією, функція викликає саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він є обробленим для копіювання.

# 3. Копіювання файлів:
# Для кожного типу файлів створюється новий шлях у вихідній директорії, використовуючи
# розширення файлу для назви піддиректорії.
# Файл з відповідним типом копіюється у відповідну піддиректорію.

# 4. Обробка винятків: код обробляє винятки, наприклад, помилки доступу до файлів або директорій.

# 5. Після виконання програми всі файли у вихідній директорії рекурсивно скопійовано в нову
# директорію та розсортовано в піддиректорії за їх розширенням.


import os
import sys
import shutil
from pathlib import Path


def parse_arguments():
    """Парсинг аргументів командного рядка"""
    if len(sys.argv) < 2:
        print("Потрібно вказати принаймні вихідну директорію\n"
              "Використання: python 01.py <source_directory> [<output_directory>]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) >= 3 else "dist"

    return input_dir, output_dir


def read_directory(source_path, output_root):
    """Рекурсивна обробка директорії та копіювання файлів"""
    try:
        with os.scandir(source_path) as items:
            for item in items:
                if item.is_dir():
                    # Рекурсивний виклик для піддиректорій
                    read_directory(item.path, output_root)
                elif item.is_file():
                    # Обробка файлу
                    sort_file_by_extension(item.path, output_root)
    except PermissionError as e:
        print(f"Помилка доступу до директорії {source_path}: {e}")
    except Exception as e:
        print(f"Неочікувана помилка {source_path}: {e}")


def sort_file_by_extension(file_path, output_root):
    """Копіює файл у піддиректорію, що відповідає його розширенню"""
    try:
        # Визначення розширення файлу
        file_ext = Path(file_path).suffix.lower()
        if not file_ext:  # якщо файл не має розширення
            file_ext = "no_extension"
        else:
            file_ext = file_ext[1:]  # прибрати крапку з початку

        # Створення шляху призначення
        output_dir = os.path.join(output_root, file_ext)
        os.makedirs(output_dir, exist_ok=True)

        # Копіювання файлу
        output_path = os.path.join(output_dir, os.path.basename(file_path))
        shutil.copy2(file_path, output_path)
        print(f"Скопійовано {file_path} -> {output_path}")

    except PermissionError as e:
        print(f"Помилка доступу до файлу {file_path}: {e}")
    except Exception as e:
        print(f"Неочікувана помилка {file_path}: {e}")


def main():
    # Парсинг аргументів
    source_dir, output_dir = parse_arguments()

    # Перевірка чи існує вихідна директорія
    if not os.path.exists(source_dir):
        print(f"Вихідна директорія {source_dir} не існує")
        sys.exit(1)

    # Створення директорії призначення (якщо не існує)
    os.makedirs(output_dir, exist_ok=True)

    # Обробка вихідної директорії
    print(f"Початок обробки. \nВихідна директорія: {source_dir}, \nПризначення: {output_dir}")
    read_directory(source_dir, output_dir)
    print("Обробку завершено")


# python 01.py d:\Temp\ d:\Temp_dist
if __name__ == "__main__":
    main()
