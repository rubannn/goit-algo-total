import networkx as nx
import matplotlib.pyplot as plt
import random
from tabulate import tabulate


# Алгоритм Дейкстри для пошуку найкоротшого шляху в графі
def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


graph = {
    "A": {"B": 5},
    "B": {"A": 5, "C": 3},
    "C": {"B": 3, "D": 2, "R": 7, "S": 1},
    "D": {"C": 2, "E": 4},
    "E": {"D": 4, "F": 6, "K": 2, "L": 3},
    "F": {"E": 6, "L": 1},
    "G": {"H": 2},
    "H": {"G": 2, "I": 5},
    "I": {"H": 5, "K": 3, "P": 2, "R": 4},
    "K": {"I": 3, "E": 2},
    "L": {"E": 3, "F": 1, "M": 2},
    "M": {"L": 2},
    "O": {"P": 3},
    "P": {"O": 3, "I": 2},
    "R": {"I": 4, "C": 7},
    "S": {"C": 1, "T": 5},
    "T": {"S": 5},
}


# Обчислюємо найкоротші шляхи для всіх вершин
all_pathes = {}
vertices = sorted(graph.keys())
for vertex in vertices:
    all_pathes[vertex] = dijkstra(graph, vertex)

# Створюємо матрицю відстаней
distance_matrix = []
headers = ["From/To"] + vertices
for from_vertex in vertices:
    row = [from_vertex]
    for to_vertex in vertices:
        distance = all_pathes[from_vertex][to_vertex]
        row.append(distance if distance != float("infinity") else "∞")
    distance_matrix.append(row)

# Виводимо матрицю відстаней у вигляді таблиці
print("\nМатриця найкоротших відстаней між всіма вершинами:")
print(tabulate(distance_matrix, headers=headers, tablefmt="grid"))

# початкова_вершина
start_vertex = random.choice(list(graph.keys()))

# Знаходимо найдальшу вершину від стартової
pathes = all_pathes[start_vertex]
far_node = max(pathes, key=lambda k: pathes[k])
red_nodes = [far_node, start_vertex]

# Візуалізація графа
G = nx.Graph(graph)
pos = nx.spring_layout(G, seed=42)

for vertex in graph:
    for neighbor, weight in graph[vertex].items():
        G.add_edge(vertex, neighbor, weight=weight)

plt.figure(figsize=(12, 8))

# Створюємо інформативний заголовок
title = f"Граф з вагами ребер\nПочаткова вершина: {start_vertex} | Найвіддаленіша вершина: {far_node} | Відстань: {pathes[far_node]}"
node_size = 600

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=node_size,
    font_weight="bold",
)

# Виділяємо початкову та найвіддаленішу вершини
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[start_vertex],
    node_color="green",
    node_size=node_size,
    label=f"Початкова ({start_vertex})",
)
nx.draw_networkx_nodes(
    G,
    pos,
    nodelist=[far_node],
    node_color="red",
    node_size=node_size,
    label=f"Найвіддаленіша ({far_node}, відстань={pathes[far_node]})",
)

# Додаємо підписи ваг ребер
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Додаємо легенду
plt.legend(scatterpoints=1, frameon=True, labelspacing=2, title="Вершини:")

plt.title(title, pad=20)
plt.show()
