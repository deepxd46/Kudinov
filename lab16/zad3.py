import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value      # Значение узла 
        self.left = None        # Левый потомок
        self.right = None       # Правый потомок

def insert_bst(root, value): # Вставка значения
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def find_node(root, value): # Ищем узел с заданным значением
    current = root
    while current:
        if value == current.value:
            return current
        elif value < current.value:
            current = current.left
        else:
            current = current.right
    return None

def can_reach(root, from_val, to_val):
    # Находим узел from_val
    from_node = find_node(root, from_val)
    if not from_node:
        print(f"Узел с значением {from_val} не найден в дереве.")
        return False

    # Рекурсивная функция для поиска to_val в поддереве from_node
    def _is_descendant(node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        return _is_descendant(node.left, target) or _is_descendant(node.right, target)

    return _is_descendant(from_node, to_val)

def draw_binary_tree(root, title="Бинарное дерево"): # Рисование бинарного дерева
    G = nx.DiGraph()  # Направленный граф для отображения связей

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
            # Рекурсивно вычисляю позиции для левого и правого поддеревьев
            _compute_positions(node.left, depth + 1, pos_x - 1, positions)
            _compute_positions(node.right, depth + 1, pos_x + 1, positions)
        return positions

    positions = _compute_positions(root)

    # Рисуем узлы
    nx.draw_networkx_nodes(G, positions, node_size=800, node_color='lightblue')

    # Рисуем ребера
    nx.draw_networkx_edges(G, positions, arrows=True, arrowstyle='-|>', arrowsize=20)

    # Рисуем метоки узла
    nx.draw_networkx_labels(G, positions, labels, font_size=12, font_weight='bold')

    # Отображение
    plt.title(title)
    plt.axis('off')
    plt.show()

def main(): # Пример использования
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

    print("Бинарное дерево:")
    draw_binary_tree(root, title="Бинарное дерево")

    # Примеры проверок
    test_cases = [
        (15, 12),  # True (12 - потомок 15)
        (10, 17),  # False (17 не потомок 10)
        (20, 25),  # True (25 - потомок 20)
        (8, 15),   # False (15 не потомок 8)
        (10, 10),  # True (узел является своим потомком)
        (30, 10),  # False (30 не существует в дереве)
    ]

    for from_val, to_val in test_cases:
        result = can_reach(root, from_val, to_val)
        print(f"Можно ли добраться из {from_val} в {to_val}? {'Да' if result else 'Нет'}")

if __name__ == "__main__":
    main()
