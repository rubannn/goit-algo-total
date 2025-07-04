import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None and node.val is not None:  # Check for None values
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left and node.left.val is not None:
            graph.add_edge(node.id, node.left.id)
            L = x - 1 / 2**layer
            pos[node.left.id] = (L, y - 1)
            L = add_edges(graph, node.left, pos, x=L, y=y - 1, layer=layer + 1)
        if node.right and node.right.val is not None:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(heap_array):
    if not heap_array:
        return None

    # Створюємо вузли для кожного елемента купи
    nodes = [Node(val) for val in heap_array]

    # Зв'язуємо вузли відповідно до структури купи
    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]

    return nodes[0]  # Повертаємо корінь дерева


# # Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

# # Відображення дерева
# draw_tree(root)

# Приклад бінарної мінімальної купи у вигляді масиву
heap_array = [0, 4, 1, 5, 10, 3, 2, 6, 7, 8, 9, None, None, 17, None, None, None, None, 20]

# Побудова дерева з купи
heap_tree_root = build_heap_tree(heap_array)

# Візуалізація дерева
draw_tree(heap_tree_root)
