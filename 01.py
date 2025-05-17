import heapq


def minimal_cable_connection_cost(cables):
    if not cables:
        return 0

    # Перетворюємо список у купу
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Витягуємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        print(f"З'єднуємо кабелі {first} і {second} - вартість {first + second}")
        # Обчислюємо вартість їх з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6, 8, 5]
print("Мінімальні загальні витрати:", minimal_cable_connection_cost(cables))
