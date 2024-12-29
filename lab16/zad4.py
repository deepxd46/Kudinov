import networkx as nx
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value      # Значение узла
        self.left = None        # Левый потомок
        self.right = None       # Правый потомок

def insert_bst(root, value):
    # Вставка значения
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def count_occurrences(root, target):
    # Подсчет количества вхождений
    if root is None:
        return 0
    count = 0
    if root.value == target:
        count += 1
    # Рекурсивно считаю в левом и правом поддеревьях
    count += count_occurrences(root.left, target)
    count += count_occurrences(root.right, target)
    return count

def draw_binary_tree(root, title="Бинарное дерево"): # Рисует бинарное дерево
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

    # Вычисление позиций узлов
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

    # Добавление меток
    nx.draw_networkx_labels(G, positions, labels, font_size=12, font_weight='bold')

    # Отображение графика
    plt.title(title)
    plt.axis('off')  
    plt.show()

def main():
    # Пример бинарного дерева поиска с дубликатами
    """
            15
           /  \
         10    20
         / \   / \
        8  12 17 25
             \
             15  # Дубликат
    """
    root = None
    values = [15, 10, 20, 8, 12, 17, 25, 15]  # Вставка дубликата 15
    for val in values:
        root = insert_bst(root, val)

    print("Бинарное дерево:")
    draw_binary_tree(root, title="Бинарное дерево")

    # Пример подсчёта вхождений
    test_values = [15, 10, 20, 8, 12, 17, 25, 30]

    for val in test_values:
        count = count_occurrences(root, val)
        print(f"Число вхождений элемента {val}: {count}")

if __name__ == "__main__":
    main()
