import tkinter as tk
from tkinter import messagebox

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def perform_dfs():
    try:
        raw_data = input_field.get("1.0", tk.END).strip()
        if not raw_data:
            raise ValueError("Please enter the graph in the specified format.")

        graph = parse_adjacency_list(raw_data)
        start_node = start_node_entry.get().strip()
        if start_node not in graph:
            raise ValueError("Start node is not present in the graph.")
        
        visited = dfs(graph, start_node)

        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, f"Visited nodes: {', '.join(visited)}")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while processing the graph:\n{e}")

def parse_adjacency_list(raw_data):
    graph = {}
    for line in raw_data.splitlines():
        parts = line.split()
        node, neighbors = parts[0], parts[1:]
        graph[node] = neighbors
    return graph

# Create the main window
root = tk.Tk()
root.title("DFS Algorithm")

# Instructions
instructions = (
    "Enter the graph as an adjacency list. Each line should contain a node followed by its neighbors.\n"
    "For example:\n"
    "A B C\n"
    "B D\n"
    "C D\n"
    "D\n"
)
tk.Label(root, text=instructions, font=("Arial", 10), justify="left").pack(pady=10)

# Input field for the adjacency list
input_field = tk.Text(root, height=10, width=50, font=("Arial", 12))
input_field.pack(pady=10)

# Input field for the start node
tk.Label(root, text="Enter Start Node:", font=("Arial", 10)).pack(pady=5)
start_node_entry = tk.Entry(root, font=("Arial", 12))
start_node_entry.pack(pady=5)

# Button to perform DFS
tk.Button(root, text="Perform DFS", command=perform_dfs, font=("Arial", 12)).pack(pady=10)

# Output area for results
tk.Label(root, text="Visited Nodes:", font=("Arial", 12)).pack(pady=5)
output_area = tk.Text(root, height=5, width=50, font=("Arial", 12))
output_area.pack(pady=10)

root.geometry("600x700")

# Run the application
root.mainloop()