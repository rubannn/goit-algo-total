import turtle
import random


def pythagoras_tree(t, size, depth, angle=45):
    """Рекурсивна функція для малювання дерева Піфагора

    Аргументи:
        t: об'єкт черепашки
        size: довжина поточної гілки
        depth: рівень рекурсії (глибина дерева)
        angle: кут розгалуження гілок
    """
    if depth == 0:  # Базовий випадок рекурсії
        return

    # Малюємо поточну гілку (стовбур)
    t.forward(size)

    # Зберігаємо позицію та напрямок для правої гілки
    pos = t.position()
    heading = t.heading()

    # Малюємо праву гілку
    t.right(angle)
    pythagoras_tree(t, size * 0.7, depth - 1, angle)

    # Повертаємось до збереженої позиції
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

    # Малюємо ліву гілку
    t.left(angle)
    pythagoras_tree(t, size * 0.7, depth - 1, angle)

    # Повертаємось до збереженої позиції
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()


def draw_pythagoras_tree():
    """Функція для налаштування та малювання дерева"""

    # Налаштування графічного вікна
    window = turtle.Screen()
    window.bgcolor("white")

    # level_str = f"{random.randint(3, 7)}"
    level_str = turtle.textinput("Рівень рекурсії", "Введіть рівень рекурсії (3-7):")

    if level_str is None:  # Якщо натиснуто Cancel
        turtle.bye()
        return None

    try:
        level = int(level_str)
        if level < 3 or level > 7:
            raise ValueError("Рівень рекурсії повинен бути від 3 до 7.")
    except ValueError as e:
        turtle.bye()
        print(f"Помилка: {e}")
        return None

    window.title(f"Дерево Піфагора (рівень={level})")

    # Створення та налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.width(2)
    t.pendown()

    # Випадковий кут розгалуження між 30 і 60 градусами
    branch_angle = random.randint(30, 60)

    # Починаємо малювання дерева
    pythagoras_tree(t, 100, level, branch_angle)

    # Завершуємо роботу
    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    draw_pythagoras_tree()
