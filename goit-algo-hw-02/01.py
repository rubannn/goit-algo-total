# Код виконується, використано клас Queue з модуля queue в Python.
# Програма автоматично генерує нові заявки, додає їх до черги, а потім послідовно видаляє з черги.
# Структура коду відповідає наданому псевдокоду.
# ==========================================================
# import Queue

# Створити чергу заявок
# queue = Queue()

# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок


from queue import Queue
import random
import time

q = Queue()
id_counter = 1


def generate_request():
    """Створює нову заявку та додає її до черги."""
    global id_counter
    request_data = {
        "id": id_counter,
        "description": f"Заявка #{id_counter}",
    }
    q.put(request_data)
    print(f"Створено нову заявку: ID {id_counter}")
    id_counter += 1


def process_request():
    if not q.empty():
        request = q.get()
        print(f"Обробляється заявка ID {request['id']} ({request['description']})")
        # Обробка заявки
        time.sleep(random.uniform(0.5, 3))
        print(f"Заявка ID {request['id']} оброблена успішно!\n")
    else:
        print("Черга пуста")


print("Початок роботи. Для виходу натисніть Ctrl+C")
try:

    while True:
        # Виклик функції для генерації нових заявок
        generate_request()

        # Виклик функції для обробки заявок
        process_request()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nВихід з програми...")
