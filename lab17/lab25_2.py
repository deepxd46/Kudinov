import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    pos = nx.spring_layout(graph)  # Определяет позиции узлов
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Граф")
    plt.show()