import turtle
import random


def pythagoras_tree(t, length, depth, angle=45):
    """Рекурсивна функція для малювання дерева Піфагора

    Аргументи:
        t: об'єкт черепашки
        length: довжина поточної гілки
        depth: рівень рекурсії (глибина дерева)
        angle: кут розгалуження гілок
    """
    if depth == 0:  # Базовий випадок рекурсії
        return

    # Малюємо поточну гілку (стовбур)
    t.forward(length)

    # Зберігаємо позицію та напрямок для правої гілки
    pos = t.position()  # Запам'ятовуємо поточні координати
    heading = t.heading()  # Запам'ятовуємо поточний кут напрямку

    # Малюємо праву гілку
    t.right(angle)  # Поворот на заданий кут вправо
    pythagoras_tree(
        t, length * 0.7, depth - 1, angle
    )  # Рекурсивний виклик для правої гілки

    # Повертаємось до збереженої позиції
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    # Малюємо ліву гілку
    t.left(angle)  # Поворот на заданий кут вліво
    pythagoras_tree(
        t, length * 0.7, depth - 1, angle
    )  # Рекурсивний виклик для лівої гілки

    # Повертаємось до збереженої позиції
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()


def draw_pythagoras_tree(level):
    """Функція для налаштування та малювання дерева"""

    # Налаштування графічного вікна
    window = turtle.Screen()
    window.bgcolor("white")  # Білий фон
    window.title(f"Дерево Піфагора (рівень={level})")  # Заголовок вікна

    # Створення та налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)  # Найшвидша швидкість малювання
    t.color("green")
    t.penup()

    # Початкова позиція черепашки (центруємо дерево)
    t.goto(0, -200)
    t.setheading(90)
    t.width(2)

    # Випадковий кут розгалуження між 30 і 60 градусами
    branch_angle = random.randint(30, 60)

    # Починаємо малювання дерева
    pythagoras_tree(t, 100, level, branch_angle)

    # Завершуємо роботу
    t.hideturtle()  # Ховаємо черепашку
    window.mainloop()  # Тримаємо вікно відкритим


if __name__ == "__main__":
    # Випадково обираємо рівень рекурсії від 3 до 7
    # Для рівнів менше 3 дерево буде занадто простим,
    # більше 7 - занадто складним і довгим у малюванні
    
    # recursion_level = random.randint(3, 7)
    recursion_level = int(input("Введіть рівень рекурсії (3-7): "))

    # Запускаємо малювання дерева
    draw_pythagoras_tree(recursion_level)
