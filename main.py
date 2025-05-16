import timeit

# Номінали монет
COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми
    min_coins = [0] + [float("inf")] * amount
    # Масив для зберігання останньої монети, яку було використано
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    # Відновлення рішення
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


# Тестові суми
test_values = [100, 432, 999, 1500, 3000, 5000]
repeat_count = 100

# Таблиця результатів
header = f"| {'Тестове значення':^20} | {'find_coins_greedy (сек)':^25} | {'find_min_coins (сек)':^25} |"
row_separator = "-" * len(header)
print(f"{row_separator}\n{header}\n{row_separator}")

for value in test_values:
    time_greedy = timeit.timeit(lambda: find_coins_greedy(value), number=repeat_count)
    time_min = timeit.timeit(lambda: find_min_coins(value), number=repeat_count)

    print(f"| {value:^20} | {time_greedy:^25.6f} | {time_min:^25.6f} |")

print(f"{row_separator}")
