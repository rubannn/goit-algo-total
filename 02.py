from collections import deque
import random


def dfs_iterative(graph, start_vertex):
    visited = set()
    visited_order = []
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            # Відвідуємо вершину
            visited.add(vertex)
            # Якщо не була відвідана, додаємо її до списку відвіданих вершин
            visited_order.append(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))
    return visited_order


def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])
    visited_order = []

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, додаємо її до списку відвіданих вершин
            visited_order.append(vertex)

            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited_order


graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "D", "R", "S"],
    "D": ["C", "E"],
    "E": ["D", "F", "K", "L"],
    "F": ["E", "L"],
    "G": ["H"],
    "H": ["G", "I"],
    "I": ["H", "K", "P", "R"],
    "K": ["I", "E"],
    "L": ["E", "F", "M"],
    "M": ["L"],
    "O": ["P"],
    "P": ["O", "I"],
    "R": ["I", "C"],
    "S": ["C", "T"],
    "T": ["S"],
}

# початкова_вершина
start_vertex = random.choice(list(graph.keys()))
print("Start vertex:", start_vertex)

print("DFS:\t", " ".join(dfs_iterative(graph, start_vertex)))
print("BFS:\t", " ".join(bfs_iterative(graph, start_vertex)))
