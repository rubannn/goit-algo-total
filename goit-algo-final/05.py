import uuid
import networkx as nx
import matplotlib.pyplot as plt
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
            L = x - 1 / 2**layer
            pos[node.left.id] = (L, y - 1)
            add_edges(graph, node.left, pos, x=L, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, ax, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=1500,
        node_color=colors,
        ax=ax,
    )
    ax.set_title(title)


def build_heap_tree(heap_array):
    """Створює бінарне дерево з масиву, що представляє купу."""
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
    """Генерує колір від темного до світлого залежно від кроку обходу"""
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
    """Підраховує загальну кількість вузлів у дереві"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Приклад бінарної мінімальної купи
heap_array = [0, 4, 1, 5, 10, 3, 2, 6, 7, 8, 9]

# Створюємо фігуру з трьома subplot'ами
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# 1. Исходное дерево
heap_tree_root = build_heap_tree(heap_array)
draw_tree(heap_tree_root, ax1, "Original Heap Tree")

# 2. DFS обход
heap_tree_root_dfs = build_heap_tree(heap_array)
dfs_order = depth_first_traversal(heap_tree_root_dfs)
draw_tree(
    heap_tree_root_dfs, ax2, f"DFS Traversal\nOrder: {' → '.join(map(str, dfs_order))}"
)

# 3. BFS обход
heap_tree_root_bfs = build_heap_tree(heap_array)
bfs_order = breadth_first_traversal(heap_tree_root_bfs)
draw_tree(
    heap_tree_root_bfs, ax3, f"BFS Traversal\nOrder: {' → '.join(map(str, bfs_order))}"
)

plt.tight_layout()
plt.show()
