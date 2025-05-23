import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    paths = {vertex: [] for vertex in graph}
    paths[start] = [start]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(heap, (distance, neighbor))

    return distances, paths


def draw_graph(graph, start_vertex, distances, paths, legend):
    G = nx.DiGraph()

    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))

    # Визначаємо кольори вершин
    node_colors = [
        "lightgreen" if node == start_vertex else "lightblue" for node in G.nodes()
    ]

    # Малюємо граф
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, arrowstyle="-", arrowsize=20, width=1)
    nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")

    # Додаємо ваги ребер
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    # Додаємо інформацію про відстані
    for node, (x, y) in pos.items():
        plt.text(
            x,
            y + 0.1,
            s=f"dist={distances[node]}",
            bbox=dict(facecolor="white", alpha=0.1),
            horizontalalignment="center",
        )

    plt.title(
        f"Алгоритм Дейкстри. Стартова вершина: {start_vertex}",
        size=12,
    )
    plt.axis("off")

    # Додаємо легенду (виправлено тут - використовуємо distances замість d)
    plt.text(
        -1.5,
        -1.2,
        legend,
        fontsize=10,
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plt.tight_layout()
    plt.show()


# Приклад графу
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

# початкова_вершина
start_vertex = random.choice(list(graph.keys()))

# Запускаємо алгоритм Дейкстри
distances, paths = dijkstra(graph, start_vertex)

# Виводимо результати в консоль
print(f"Найкоротші шляхи від вершини '{start_vertex}':")

legend = ""
for vertex in distances:
    legend += (
        f"{start_vertex} → {vertex}: {distances[vertex]} ({' → '.join(paths[vertex])})\n"
    )

print(legend)

# Візуалізуємо граф з результатами
draw_graph(graph, start_vertex, distances, paths, legend)
