class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_max_value(root):
    """
    Функція для знаходження найбільшого значення в BST.
    У BST найбільше значення завжди знаходиться у крайньому правому вузлі.
    """
    current = root
    while current.right is not None:
        current = current.right
    return current.val


def find_min_value(root):
    """
    Функція для знаходження найменшого значення в BST.
    У BST найменше значення завжди знаходиться у крайньому лівому вузлі.
    """
    current = root
    while current.left is not None:
        current = current.left
    return current.val


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
    Функція для виведення дерева
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
    keys = [50, 30, 20, 40, 90, 70, 10, 80, 10, 25]
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

    # Знаходимо найбільше значення
    max_value = find_max_value(root)
    print("\nНайбільше значення в дереві:", max_value)

    # Знаходимо найменше значення
    min_value = find_min_value(root)
    print("\nНайменше значення в дереві:", min_value)
