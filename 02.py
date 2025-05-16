import numpy as np
import matplotlib.pyplot as plt

# Параметри трилисника
theta = np.linspace(0, 2 * np.pi, 1000)
r = np.sin(3 * theta)
x_curve = r * np.cos(theta)
y_curve = r * np.sin(theta)

# Межі інтегрування (можна змінювати)
x_min, x_max = 0, 1.0  # Межі по x
y_min, y_max = -1.0, 1.0  # Межі по y

# Площа прямокутника для методу Монте-Карло
area_rectangle = (x_max - x_min) * (y_max - y_min)

# Кількість випадкових точок
N = 50000

# Генерація випадкових точок у прямокутнику
x_random = np.random.uniform(x_min, x_max, N)
y_random = np.random.uniform(y_min, y_max, N)

# Відкидаємо точки поза одиничним колом (бо трилисник обмежений колом)
r_random = np.sqrt(x_random**2 + y_random**2)
in_circle = (
    (r_random <= 1)
    & (x_random >= x_min)
    & (x_random <= x_max)
    & (y_random >= y_min)
    & (y_random <= y_max)
)
x_in = x_random[in_circle]
y_in = y_random[in_circle]

# Перевірка, чи точка всередині трилисника
theta_in = np.arctan2(y_in, x_in)
theta_in = np.mod(theta_in, 2 * np.pi)  # Приводимо до [0, 2π]
r_in = np.sqrt(x_in**2 + y_in**2)
r_polar = np.sin(3 * theta_in)

# Враховуємо тільки позитивні значення r
inside = (r_polar >= 0) & (r_in <= r_polar)

# Обчислення площі методом Монте-Карло
# Відношення точок всередині трилисника до точок у прямокутнику, помножене на площу прямокутника
area_estimate = (np.sum(inside) / N) * area_rectangle

# Точна площа трилисника (3 пелюстки, кожна з площею π/12)
A_exact = np.pi / 4 / 2  # Загальна площа: 3 * (π/12) / 2 = π/8

# Візуалізація
plt.figure(figsize=(10, 8))
plt.plot(x_curve, y_curve, color="blue", linewidth=2, label="Контур трилисника")

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
    x_in[inside],
    y_in[inside],
    color="green",
    s=1,
    alpha=0.6,
    label="Точки всередині трилисника",
)
plt.scatter(
    x_in[~inside],
    y_in[~inside],
    color="red",
    s=1,
    alpha=0.2,
    label="Точки поза трилисником",
)

# Стилізація графіка
plt.title(
    f"Оцінка площі трилисника методом Монте-Карло\nМежі: x ∈ [{x_min}, {x_max}], y ∈ [{y_min}, {y_max}]",
    fontsize=14,
)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")
plt.tight_layout()

# Виведення результатів
print(f"Межі інтегрування: x ∈ [{x_min}, {x_max}], y ∈ [{y_min}, {y_max}]")
print(f"Оцінка площі (Монте-Карло): {area_estimate:.5f}")
print(f"Точна площа (π/4): {A_exact:.5f}")
print(f"Похибка: {abs(area_estimate - A_exact):.5f}")

plt.show()
