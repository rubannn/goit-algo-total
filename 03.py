import networkx as nx
import matplotlib.pyplot as plt


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

start_node = "A"
pathes = dijkstra(graph, start_node)
print(pathes)

# Знаходимо найдальшу вершину від стартової
far_node = max(pathes, key=lambda k: pathes[k])
red_nodes = [far_node, start_node]


G = nx.Graph(graph)
pos = nx.spring_layout(G, seed=42)

for vertex in graph:
    for neighbor, weight in graph[vertex].items():
        G.add_edge(vertex, neighbor, weight=weight)

nx.draw(
    G, pos, with_labels=True, node_color="lightblue", node_size=600, font_weight="bold"
)

# Додаємо підписи ваг ребер (опціонально)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

nx.draw_networkx_nodes(G, pos, nodelist=red_nodes, node_color="red", node_size=800)


plt.title("Граф з вагами ребер")
plt.show()
