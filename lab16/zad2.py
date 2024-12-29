import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value      # Значение узла 
        self.left = None        # Левый потомок
        self.right = None       # Правый потомок

def insert_bst(root, value): # Вставка значения в BST
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def find_min(root): # Минимальное значение в BST
    current = root
    while current.left is not None:
        current = current.left
    return current

def find_max(root): # Максимальное значение в BST
    current = root
    while current.right is not None:
        current = current.right
    return current

def delete_node(root, value): # Удаление узла из BST
    if root is None:
        return root

    # Если значение меньше, чем значение корня, ищем в левом поддереве
    if value < root.value:
        root.left = delete_node(root.left, value)
    # Если значение больше, чем значение корня, ищем в правом поддереве
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # Узел с одним потомком или без потомков
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Узел с двумя потомками:
        # Находим минимальное значение из правого поддерева
        temp = find_min(root.right)
        root.value = temp.value
        # Удаляем минимальный узел из правого поддерева
        root.right = delete_node(root.right, temp.value)

    return root

def draw_binary_tree(root, title="Бинарное дерево"): # Рисование бинарного дерева
    G = nx.DiGraph()  # Направленный граф для показа связей

    labels = {}
    def _add_edges(node, parent=None):
        if node is not None:
            labels[node.value] = str(node.value)
            if parent is not None:
                G.add_edge(parent.value, node.value)
            _add_edges(node.left, node)
            _add_edges(node.right, node)

    _add_edges(root)

    # Функция для вычисления позиций узлов
    def _compute_positions(node, depth=0, pos_x=0, positions={}):
        if node is not None:
            positions[node.value] = (pos_x, -depth)
            # Рекурсивно вычисляем позиции для левого и правого поддеревьев
            _compute_positions(node.left, depth + 1, pos_x - 1, positions)
            _compute_positions(node.right, depth + 1, pos_x + 1, positions)
        return positions

    positions = _compute_positions(root)

    # Рисуем узлы
    nx.draw_networkx_nodes(G, positions, node_size=800, node_color='lightblue')

    # Рисуем ребера
    nx.draw_networkx_edges(G, positions, arrows=True, arrowstyle='-|>', arrowsize=20)

    # Рисуем метоки узлов
    nx.draw_networkx_labels(G, positions, labels, font_size=12, font_weight='bold')

    # Отображение
    plt.title(title)
    plt.axis('off')
    plt.show()

def main(): # Пример
    """
            15
           /  \
         10    20
         / \   / \
        8  12 17 25
    """
    root = None
    values = [15, 10, 20, 8, 12, 17, 25]
    for val in values:
        root = insert_bst(root, val)

    print("Бинарное дерево до удаления:")
    draw_binary_tree(root, title="Бинарное дерево до удаления")

    # Нахождение максимального и минимального значений 
    min_node = find_min(root)
    max_node = find_max(root)
    print(f"Минимальное значение в дереве: {min_node.value}")
    print(f"Максимальное значение в дереве: {max_node.value}")

    # Удаление узлов с минимальным и максимальным значениями
    root = delete_node(root, min_node.value)
    root = delete_node(root, max_node.value)

    print("Бинарное дерево после удаления:")
    draw_binary_tree(root, title="Бинарное дерево после удаления")

if __name__ == "__main__":
    main()
