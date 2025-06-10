import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Задана функція
def func(x):
    return (
        2 * np.exp(-((x - 3) ** 2))
        + 3 * np.exp(-0.5 * (x - 6) ** 2)
        + 4 * np.exp(-0.5 * (x - 9) ** 2)
    )


# Межі інтегрування
x_min, x_max = 4, 9
y_min, y_max = 0, 5  # Верхня межа обрана з урахуванням максимального значення функції

# Площа прямокутника для методу Монте-Карло
area_rectangle = (x_max - x_min) * (y_max - y_min)

# Кількість випадкових точок
N = 50000

# Генерація випадкових точок у прямокутнику
x_random = np.random.uniform(x_min, x_max, N)
y_random = np.random.uniform(y_min, y_max, N)

# Обчислення значень функції для випадкових x
y_func = func(x_random)

# Визначення точок, які знаходяться під кривою (всередині області інтегрування)
inside = y_random <= y_func

# Обчислення площі методом Монте-Карло
area_estimate = (np.sum(inside) / N) * area_rectangle

# Візуалізація
x_plot = np.linspace(0, 15, 1000)
y_plot = func(x_plot)

plt.figure(figsize=(10, 8))
plt.plot(x_plot, y_plot, color="blue", linewidth=2, label="Функція")

# Додаємо межі інтегрування (прямокутник)
plt.plot(
    [x_min, x_max, x_max, x_min, x_min],
    [y_min, y_min, y_max, y_max, y_min],
    color="black",
    linestyle="--",
    linewidth=1,
    label="Межі інтегрування",
)

plt.scatter(
    x_random[inside],
    y_random[inside],
    color="green",
    s=1,
    alpha=0.6,
    label="Точки під кривою",
)
plt.scatter(
    x_random[~inside],
    y_random[~inside],
    color="red",
    s=1,
    alpha=0.2,
    label="Точки над кривою",
)

# Стилізація графіка
plt.title(
    f"Оцінка інтегралу методом Монте-Карло\nМежі: x ∈ [{x_min}, {x_max}], y ∈ [{y_min}, {y_max}]",
    fontsize=14,
)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()

# Виведення результатів
print(f"Межі інтегрування: x ∈ [{x_min}, {x_max}], y ∈ [{y_min}, {y_max}]")
print(f"Оцінка інтегралу (Монте-Карло): {area_estimate:.5f}")

exact_integral, _ = quad(func, x_min, x_max)
print(f"Точний інтеграл: {exact_integral:.5f}")
print(f"Похибка: {abs(area_estimate - exact_integral):.5f}")
plt.show()
