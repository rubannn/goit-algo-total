class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def tree_sum(root):
    """
    Функція для знаходження суми всіх значень у дереві.
    Використовує рекурсивний підхід.
    """
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def insert(root, key):
    """
    Функція для вставки нового вузла в BST
    """
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def print_tree(root, level=0, prefix="Root: "):
    """
    Функція для виведення дерева в консоль з відступами
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


def create_sample_tree():
    """
    Створення та заповнення дерева з 10 вузлів
    """
    keys = [50, 30, 20, 40, 70, 60, 80, 10, 25, 90]
    root = None
    for key in keys:
        root = insert(root, key)
    return root


if __name__ == "__main__":
    # Створюємо дерево
    root = create_sample_tree()

    # Виводимо дерево
    print("Двійкове дерево пошуку:")
    print_tree(root)

    # Знаходимо суму всіх значень
    total_sum = tree_sum(root)
    print("\nСума всіх значень у дереві:", total_sum)
