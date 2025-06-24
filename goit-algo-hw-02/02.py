# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до
# двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців
# черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з
# парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.


from collections import deque


def is_palindrome(s):
    # Створюємо двосторонню чергу
    dq = deque(c.lower() for c in s)

    while len(dq) > 1:
        left = dq.popleft()
        last = dq.pop()
        if left != last:
            return False

    return True


tests = [
    "aBracadabra",
    "text",
    "12321",
    "abradadarba",
    "яемзмея",
    "АрозаупаланалапуАзора",
]

for s in tests:
    print(f"'{s}' — паліндром? {is_palindrome(s)}")
