# Напишіть програму на Python, яка використовує рекурсію для створення фракталу
# «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.

import turtle
import random


def koch_curve(t, size, depth):
    if depth == 0:
        t.forward(size)
    else:
        size /= 3.0
        # koch_curve(t, size, depth - 1)
        # t.left(60)
        # koch_curve(t, size, depth - 1)
        # t.right(120)
        # koch_curve(t, size, depth - 1)
        # t.left(60)
        # koch_curve(t, size, depth - 1)

        for angle in [60, -120, 60, 0]:
            koch_curve(t, size, depth - 1)
            t.left(angle)
        # koch_curve(t, size, depth - 1)


def draw_koch_snowflake():
    # Налаштування вікна
    window = turtle.Screen()
    window.bgcolor("white")

    level_str = turtle.textinput("Рівень рекурсії", "Введіть рівень рекурсії (1-5):")

    if level_str is None:  # Якщо натиснуто Cancel
        turtle.bye()
        return None

    try:
        level = int(level_str)
        if level < 1 or level > 5:
            raise ValueError("Рівень рекурсії повинен бути від 1 до 5.")
    except ValueError as e:
        turtle.bye()
        print(f"Помилка: {e}")
        return None

    window.title(f"Сніжинка Коха ({level=})")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша швидкість
    t.color("blue")
    t.penup()

    # Початкові параметри
    size = 300
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо сніжинку (3 криві Коха під кутом 120 градусів)
    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)

    # Завершення
    t.hideturtle()
    window.mainloop()


# Запуск програми
if __name__ == "__main__":
    # level = random.randint(1, 5)  # Випадковий рівень рекурсії від 1 до 5
    # level = int(input("Введіть рівень рекурсії (1-5): "))
    draw_koch_snowflake()
