import networkx as nx
import matplotlib.pyplot as plt
import lab25_2

def is_all_reachable_from_vertex(graph, start_vertex):
    visited = set()
    
    def dfs(vertex):
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                dfs(neighbor)
    
    dfs(start_vertex)
    return len(visited) == len(graph.nodes())

# Пример использования
G = nx.DiGraph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
start_vertex = 0

if is_all_reachable_from_vertex(G, start_vertex):
    print(f"Все вершины достижимы из вершины {start_vertex}")
else:
    print(f"Не все вершины достижимы из вершины {start_vertex}")

# Визуализация графа
lab25_2.draw_graph(G)

