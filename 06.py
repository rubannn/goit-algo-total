import random


def greedy_algorithm(items, budget):
    # Створюємо список страв з їх характеристиками та співвідношенням калорій/вартість
    item_list = []
    for name, props in items.items():
        ratio = props["calories"] / props["cost"]
        item_list.append((name, props["cost"], props["calories"], ratio))

    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    item_list.sort(key=lambda x: x[3], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item in item_list:
        name, cost, calories, _ = item
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def dynamic_programming(items, budget):
    # Перетворюємо словник у список для зручності
    item_list = []
    for name, props in items.items():
        item_list.append((name, props["cost"], props["calories"]))

    n = len(item_list)
    # Ініціалізуємо таблицю DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        name, cost, calories = item_list[i - 1]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначаємо, які страви були обрані
    w = budget
    selected_items = []
    total_calories = dp[n][budget]
    total_cost = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, cost, calories = item_list[i - 1]
            selected_items.append(name)
            w -= cost
            total_cost += cost

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = random.randint(100, 200)  # Випадковий бюджет від 100 до 200
print(f"Бюджет: {budget} грн\n")

print("Жадібний алгоритм:")
result_ga = greedy_algorithm(items, budget)
for key in result_ga:
    print(f"{key}: {result_ga[key]}")

print("\nДинамічне програмування:")
result_dp = dynamic_programming(items, budget)
for key in result_dp:
    print(f"{key}: {result_dp[key]}")
