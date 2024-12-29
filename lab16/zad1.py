class TreeNode:
    def __init__(self, value):
        self.value = value      # Значение узла
        self.left = None        # Левый потомок
        self.right = None       # Правый потомок

def draw_binary_tree(root):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph() # Направленный граф для показа связей

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
    def _compute_positions(node, depth=0, pos_x=0, positions={}, x_offsets={}):
        if node is not None:
            # Горизонтальное смещение узла
            if node.left:
                _compute_positions(node.left, depth + 1, pos_x - 1, positions, x_offsets)
            positions[node.value] = (pos_x, -depth)
            if node.right:
                _compute_positions(node.right, depth + 1, pos_x + 1, positions, x_offsets)
        return positions

    positions = _compute_positions(root)

    # Рисуем узлы
    nx.draw_networkx_nodes(G, positions, node_size=800, node_color='lightblue')

    # Рисуем ребра
    nx.draw_networkx_edges(G, positions, arrows=False)

    # Метки узлов, их рисование 
    nx.draw_networkx_labels(G, positions, labels, font_size=14, font_weight='bold')

    # Отображение
    plt.title("Бинарное дерево")
    plt.axis('off')  
    plt.show()

if __name__ == "__main__":
    # Пример бинарного дерева
    """
            1
           / \
          2   3
         / \   \
        4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Его визуализация
    draw_binary_tree(root)
