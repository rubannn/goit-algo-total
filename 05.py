import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal_order=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    if traversal_order:
        plt.title(f"Traversal order: {' -> '.join(map(str, traversal_order))}")

    plt.show()


def build_heap_tree(heap_array):
    if not heap_array:
        return None

    nodes = [Node(val) for val in heap_array]

    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]

    return nodes[0]


def generate_color(step, total_steps):
    """Generate a color from dark to light based on traversal step"""
    intensity = int(32 + (step / (total_steps + 1)) * 223)
    return f"#{intensity:02x}{intensity:02x}FF"


def depth_first_traversal(root):
    if not root:
        return []

    stack = [root]
    visited_order = []
    total_nodes = count_nodes(root)

    while stack:
        node = stack.pop()
        visited_order.append(node.val)
        node.color = generate_color(len(visited_order), total_nodes)

        # Додаємо спочатку правого, потім лівого нащадка, щоб лівий оброблявся першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_order


def breadth_first_traversal(root):
    if not root:
        return []

    queue = deque([root])
    visited_order = []
    total_nodes = count_nodes(root)

    while queue:
        node = queue.popleft()
        visited_order.append(node.val)
        node.color = generate_color(len(visited_order), total_nodes)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_order


def count_nodes(root):
    """Count total nodes in the tree"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Приклад бінарної мінімальної купи
heap_array = [0, 4, 1, 5, 10, 3, 2, 6, 7, 8, 9]
heap_tree_root = build_heap_tree(heap_array)

# Візуалізація дерева
print("Original tree:")
draw_tree(heap_tree_root)

# Обхід у глибину (DFS)
print("\nDepth First Traversal:")
dfs_order = depth_first_traversal(heap_tree_root)
print("Order:", dfs_order)
draw_tree(heap_tree_root, dfs_order)

# Відновлення дерева для наступного обходу
heap_tree_root = build_heap_tree(heap_array)

# Обхід у ширину (BFS)
print("\nBreadth First Traversal:")
bfs_order = breadth_first_traversal(heap_tree_root)
print("Order:", bfs_order)
draw_tree(heap_tree_root, bfs_order)
