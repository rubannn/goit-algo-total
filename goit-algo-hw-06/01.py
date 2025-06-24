import networkx as nx
import matplotlib.pyplot as plt

# Створення графа транспортної мережі (наприклад, метро)
G = nx.Graph()

# Додавання станцій (вершин)
stations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K","L", "M", "O", "P", "R", "S", "T"]
G.add_nodes_from(stations)

# Додавання ліній (ребер) між станціями метро
edges = [
    ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"),               # Лінія 1
    ("G", "H"), ("H", "I"), ("I", "K"), ("K", "E"), ("E", "L"), ("L", "M"),   # Лінія 2
    ("O", "P"), ("P", "I"), ("I", "R"), ("R", "C"), ("C", "S"), ("S", "T"),   # Лінія 3
    ("F", "L"),
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста (метро)")
plt.show()

# Аналіз основних характеристик
print("Основні характеристики графа:")
print(f"- Кількість вершин: {G.number_of_nodes()}")
print(f"- Кількість ребер: {G.number_of_edges()}")
print(f"- Ступені вершин: {dict(G.degree())}")
print(f"- Середній ступінь вершин: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")

# Додаткові метрики
print("\nДодаткові метрики:")
print(f"- Чи є граф зв'язним: {nx.is_connected(G)}")
print(f"- Діаметр графа (якщо зв'язний): {nx.diameter(G) if nx.is_connected(G) else 'не можливо обчислити'}")
print(f"- Середня довжина шляху: {nx.average_shortest_path_length(G) if nx.is_connected(G) else 'не можливо обчислити'}")
