# Напишіть програму на Python, яка використовує рекурсію для створення фракталу
# «сніжинка Коха» за умови, що користувач повинен мати можливість вказати рівень рекурсії.

import turtle


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)


def draw_koch_snowflake():
    # Налаштування вікна
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша швидкість
    t.color("blue")
    t.penup()

    # Запит рівня рекурсії у користувача
    depth = int(
        turtle.numinput(
            "Рівень рекурсії",
            "Введіть рівень рекурсії (рекомендовано 1-5):",
            default=3,
            minval=0,
            maxval=6,
        )
    )

    # Початкові параметри
    size = 300
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо сніжинку (3 криві Коха під кутом 120 градусів)
    for _ in range(3):
        koch_curve(t, size, depth)
        t.right(120)

    # Завершення
    t.hideturtle()
    window.mainloop()


# Запуск програми
if __name__ == "__main__":
    draw_koch_snowflake()
