import random
import matplotlib.pyplot as plt

# Теоретичні ймовірності для порівняння
TEORETICAL = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def simulate_dice_rolls(num_rolls):
    """Симулює кидки кубиків та повертає розподіл сум."""
    sums_count = {i: 0 for i in range(2, 13)}  # Словник для підрахунку сум

    for _ in range(num_rolls):
        # Кидаємо два кубики
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2

        # Збільшуємо лічильник для цієї суми
        sums_count[total] += 1

    # Обчислюємо ймовірності
    probabilities = {k: v / num_rolls * 100 for k, v in sums_count.items()}

    return sums_count, probabilities


def display_results(sums_count, probabilities):
    """Виводить результати симуляції у вигляді таблиці."""

    header = f"| {'Сума':^8} | {'Кількість':^10} | {'Ймовірність (%)':^15} | {'Теоретична (%)':^15} | {'Похибка (%)':^12} |"
    row_separator = "-" * len(header)

    print(f"{row_separator}\n{header}\n{row_separator}")
    # Виводимо результати для кожної суми
    for total in range(2, 13):
        count = sums_count[total]
        prob = probabilities[total]
        teor = TEORETICAL[total]
        delta = abs(prob - teor)
        print(
            f"| {total:8} | {count:^10} | {prob:15.2f} | {teor:15.2f} | {delta:^12.3f} |"
        )
    print(f"{row_separator}\n")


def plot_results(probabilities):
    """Візуалізує результати у вигляді графіка."""
    totals = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(totals, probs, color="skyblue", edgecolor="skyblue")

    plt.plot(
        totals, [TEORETICAL[t] for t in totals], "ro-", label="Теоретична ймовірність"
    )

    plt.title("Ймовірності сум при кидку двох кубиків (Метод Монте-Карло)")
    plt.xlabel("Сума чисел на кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.xticks(totals)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()


def main():
    # Кількість кидків для симуляції
    num_rolls = 1_000_000

    # Виконуємо симуляцію
    sums_count, probabilities = simulate_dice_rolls(num_rolls)

    # Виводимо результати
    print(f"\nРезультати симуляції для {num_rolls:_} кидків:")
    display_results(sums_count, probabilities)

    # Візуалізуємо результати
    plot_results(probabilities)


if __name__ == "__main__":
    main()
