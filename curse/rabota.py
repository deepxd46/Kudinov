import tkinter as tk
from tkinter import messagebox


def parse_adjacency_list(raw_data):
    graph = {}
    try:
        for line in raw_data.splitlines():
            if not line.strip():
                continue
            parts = line.split()
            node = int(parts[0])
            neighbors = list(map(int, parts[1:]))
            graph[node] = neighbors

        all_nodes = set(graph.keys()) | {neighbor for neighbors in graph.values() for neighbor in neighbors}
        for node in all_nodes:
            graph.setdefault(node, [])

    except ValueError:
        raise ValueError(
            "Ошибка: Введите список смежности в корректном формате.\n"
            "Каждая строка должна содержать узел и его соседей через пробел.\n"
            "Например: '1 2 3'."
        )
    return graph


def open_algorithm_window():
    if messagebox.askyesno("Подтверждение", "Вы точно хотите открыть новое окно?"):
        algorithm_window = tk.Toplevel(root)
        algorithm_window.title("Окно алгоритма")
        algorithm_window.geometry("1200x1000")

        instructions = (
            "Инструкция по работе:\n"
            "1. Введите граф в формате списка смежности. Каждая строка должна содержать узел и его соседей.\n"
            "   Например:\n"
            "   1 2 3\n"
            "   2 4\n"
            "   3 4\n"
            "   4\n"
            "2. Нажмите кнопку 'Выполнить алгоритм'.\n"
            "3. Результаты компонент связности и промежуточные шаги алгоритма появятся ниже."
        )
        tk.Label(algorithm_window, text=instructions, font=("Arial", 10), justify="left").pack(pady=10)

        input_field = tk.Text(algorithm_window, height=10, width=60, font=("Arial", 12))
        input_field.pack(pady=10)

        tk.Label(algorithm_window, text="Промежуточные действия:", font=("Arial", 12)).pack(pady=5)
        steps_area = tk.Text(algorithm_window, height=15, width=70, font=("Arial", 10), bg="#f7f7f7")
        steps_area.pack(pady=10)

        tk.Label(algorithm_window, text="Результат обработки:", font=("Arial", 12)).pack(pady=5)
        output_area = tk.Text(algorithm_window, height=10, width=70, font=("Arial", 12))
        output_area.pack(pady=10)

        def find_scc():
            try:
                raw_data = input_field.get("1.0", tk.END).strip()
                if not raw_data:
                    raise ValueError("Поле ввода пустое! Введите граф в указанном формате.")

                graph = parse_adjacency_list(raw_data)

                steps_area.delete("1.0", tk.END)
                output_area.delete("1.0", tk.END)

                def dfs(graph, v, visited, collector):
                    visited.add(v)
                    steps_area.insert(tk.END, f"Обходим вершину {v}\n")
                    for neighbor in graph[v]:
                        if neighbor not in visited:
                            steps_area.insert(tk.END, f"  Заходим в соседнюю вершину {neighbor}\n")
                            dfs(graph, neighbor, visited, collector)
                    collector.append(v)
                    steps_area.insert(tk.END, f"  Добавляем вершину {v} в стек или компоненту\n")

                def transpose(graph):
                    transposed = {}
                    for src in graph:
                        for dst in graph[src]:
                            transposed.setdefault(dst, []).append(src)
                    for node in graph:
                        transposed.setdefault(node, [])
                    return transposed

                def kosaraju(graph):
                    stack = []
                    visited = set()

                    steps_area.insert(tk.END, "Первый проход DFS для построения порядка завершения...\n")
                    for node in graph:
                        if node not in visited:
                            steps_area.insert(tk.END, f"Начинаем DFS с вершины {node}\n")
                            dfs(graph, node, visited, stack)

                    transposed = transpose(graph)

                    visited.clear()
                    sccs = []
                    steps_area.insert(tk.END, "Второй проход DFS для выделения компонент связности...\n")
                    while stack:
                        node = stack.pop()
                        if node not in visited:
                            component = []
                            steps_area.insert(tk.END, f"Извлекаем вершину {node} из стека и начинаем новый обход\n")
                            dfs(transposed, node, visited, component)
                            sccs.append(component)
                            steps_area.insert(tk.END, f"Найдена компонента связности: {component}\n")
                    return sccs

                sccs = kosaraju(graph)
                output_area.insert(tk.END, "Компоненты связности:\n")
                for i, component in enumerate(sccs, 1):
                    output_area.insert(tk.END, f"Компонента {i}: {component}\n")

            except ValueError as ve:
                messagebox.showerror("Ошибка ввода", str(ve))
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка при обработке графа:\n{e}")

        tk.Button(algorithm_window, text="Выполнить алгоритм", command=find_scc, font=("Arial", 12)).pack(pady=10)
        algorithm_window.resizable(False, False)


def open_info_window():
    if messagebox.askyesno("Подтверждение", "Вы точно хотите открыть окно информации?"):
        info_window = tk.Toplevel(root)
        info_window.title("Информация о программе")
        info_window.geometry("400x300")

        tk.Button(info_window, text="Описание алгоритма", font=("Arial", 12), command=show_algorithm_description).pack(pady=10)
        tk.Button(info_window, text="Информация о создателе", font=("Arial", 12), command=show_creator_info).pack(pady=10)


def show_algorithm_description():
    description = (
        "Название задания: Реализация алгоритма выделения компонент связности орграфа.\n\n"
        "Описание алгоритма:\n"
        "Алгоритм использует поиск в глубину (DFS) для выделения компонент связности в направленном графе.\n"
        "Он включает два основных этапа:\n"
        "1. Построение порядка завершения вершин при обходе графа.\n"
        "2. Поиск компонент связности в транспонированном графе."
    )
    messagebox.showinfo("Описание алгоритма", description)


def show_creator_info():
    creator_info = (
        "Программу создал:\n"
        "Пичугин Никита Антонович\n"
        "Студент направления: Информатика и вычислительная техника\n"
        "Специализация: Прикладной искусственный интеллект"
    )
    messagebox.showinfo("Информация о создателе", creator_info)


def close_window():
    if messagebox.askyesno("Подтверждение", "Вы точно хотите закрыть окно?"):
        root.destroy()


def on_close():
    if messagebox.askyesno("Подтверждение", "Вы точно хотите закрыть окно?"):
        root.destroy()


root = tk.Tk()
root.title("Реализация алгоритма")
root.geometry("400x300")

root.protocol("WM_DELETE_WINDOW", on_close)

tk.Button(root, text="Открытие алгоритма", command=open_algorithm_window, font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Информация о программе", command=open_info_window, font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Закрыть окно", command=close_window, font=("Arial", 12)).pack(pady=10)

root.mainloop()
