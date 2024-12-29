import networkx as nx
import lab25_2

def has_eulerian_cycle(graph):
    # В неориентированном графе для существования Эйлерова цикла
    # каждый вершину должно быть четное число рёбер
    if not isinstance(graph, nx.Graph):
        return False
    
    for degree in graph.degree():
        if degree[1] % 2 != 0:
            return False
    
    return True

# Пример использования
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 0), (1, 2)])

if has_eulerian_cycle(G):
    print("Граф имеет Эйлеров цикл")
else:
    print("Граф не имеет Эйлерова цикла")

# Визуализация графа
lab25_2.draw_graph(G)
