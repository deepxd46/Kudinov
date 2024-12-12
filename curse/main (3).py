import tkinter as tk
from tkinter import messagebox
import time
import random

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Глобальные списки для данных графика
nodes_list = []
times_list = []

def parse_adjacency_list(raw_data, directed=True):
    graph = {}
    try:
        for line in raw_data.splitlines():
            if not line.strip():
                continue
            parts = line.split()
            node = int(parts[0])
            neighbors = list(map(int, parts[1:]))
            graph.setdefault(node, []).extend(neighbors)
            if not directed:
                for neighbor in neighbors:
                    graph.setdefault(neighbor, []).append(node)

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


def generate_random_graph(num_nodes, edge_prob, directed=True):
    graph = {node: [] for node in range(1, num_nodes + 1)}
    for i in range(1, num_nodes + 1):
        for j in range(1, num_nodes + 1):
            if i != j and random.random() < edge_prob:
                graph[i].append(j)
                if not directed:
                    graph[j].append(i)
    return graph


def graph_to_adjacency_list(graph):
    lines = []
    for node in sorted(graph.keys()):
        neighbors = ' '.join(map(str, sorted(set(graph[node]))))
        lines.append(f"{node} {neighbors}".strip())
    return '\n'.join(lines)


def open_algorithm_window():
    if messagebox.askyesno("Подтверждение", "Вы точно хотите открыть новое окно?"):
        algorithm_window = tk.Toplevel(root)
        algorithm_window.title("Окно алгоритма")
        algorithm_window.geometry("1200x1000")
        main_frame = tk.Frame(algorithm_window)
        main_frame.pack(fill='both', expand=True)
        # Для того, чтобы не делать скролл, помещаем влево инструкцию, вправо-окна, с которыми взаимодействуем
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side='left', fill='y', padx=10, pady=10)

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        instructions = (
            "Инструкция по работе:\n"
            "1. Выберите метод ввода данных: ручной или случайный.\n"
            "2. Если выбран ручной ввод:\n"
            "   - Выберите тип графа с помощью чекбокса ниже.\n"
            "   - Введите граф в формате списка смежности. Каждая строка должна содержать узел и его соседей.\n"
            "     Например:\n"
            "     1 2 3\n"
            "     2 4\n"
            "     3 4\n"
            "     4\n"
            "3. Если выбран случайный ввод:\n"
            "   - Укажите количество узлов и вероятность ребра.\n"
            "   - Выберите тип графа с помощью чекбокса ниже.\n"
            "   - Сгенерированный граф будет отображен в поле результата.\n"
            "4. Нажмите кнопку 'Выполнить алгоритм'.\n"
            "5. Результаты компонент связности и промежуточные шаги алгоритма появятся ниже."
        )

        # Инструкции помещаем в левый фрейм
        tk.Label(left_frame, text=instructions, font=("Arial", 10), justify="left").pack(pady=10)

        # Переменная для выбора метода ввода
        input_method_var = tk.StringVar(value="manual")

        input_method_frame = tk.Frame(right_frame)
        input_method_frame.pack(pady=3)

        tk.Label(input_method_frame, text="Выберите метод ввода данных:", font=("Arial", 12)).pack(side=tk.LEFT)
        tk.Radiobutton(
            input_method_frame, text="Ручной ввод", variable=input_method_var, value="manual",
            command=lambda: toggle_input_method()
        ).pack(side=tk.LEFT)
        tk.Radiobutton(
            input_method_frame, text="Случайный ввод", variable=input_method_var, value="random",
            command=lambda: toggle_input_method()
        ).pack(side=tk.LEFT)

        is_directed_var = tk.BooleanVar(value=True)
        checkbox = tk.Checkbutton(right_frame, text="Ориентированный граф", variable=is_directed_var)
        checkbox.pack(pady=3)

        input_container_frame = tk.Frame(right_frame)
        input_container_frame.pack(pady=3)

        manual_input_frame = tk.Frame(input_container_frame)
        input_field = tk.Text(manual_input_frame, height=8, width=70, font=("Arial", 12))
        input_field.pack()
        
        random_input_frame = tk.Frame(input_container_frame)
        tk.Label(random_input_frame, text="Количество узлов:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        num_nodes_entry = tk.Entry(random_input_frame, font=("Arial", 12))
        num_nodes_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(random_input_frame, text="Вероятность ребра (0-1):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        edge_prob_entry = tk.Entry(random_input_frame, font=("Arial", 12))
        edge_prob_entry.grid(row=1, column=1, padx=5, pady=5)

        manual_input_frame.pack()

        def toggle_input_method():
            method = input_method_var.get()
            if method == "manual":
                random_input_frame.pack_forget()
                manual_input_frame.pack()
            else:
                manual_input_frame.pack_forget()
                random_input_frame.pack()

        tk.Label(right_frame, text="Промежуточные действия:",  font=("Arial", 12)).pack(pady=5)
        steps_area = tk.Text(right_frame, height=9, width=70, font=("Arial", 10))
        steps_area.pack(pady=5)

        tk.Label(right_frame, text="Результат обработки:", font=("Arial", 12)).pack(pady=5)
        output_area = tk.Text(right_frame, height=6, width=70, font=("Arial", 12))
        output_area.pack(pady=5)

        tk.Label(right_frame, text="Время выполнения алгоритма:", font=("Arial", 12)).pack(pady=5)
        time_label = tk.Label(right_frame, text="", font=("Arial", 12), width=30)
        time_label.pack(pady=5)
        # Фрейм для графика
        plot_frame = tk.Frame(left_frame)
        plot_frame.pack(pady=7)

        # Фигура для графика
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_title("Зависимость t от n-узлов")
        ax.set_xlabel("Количество узлов")
        ax.set_ylabel("Время (сек)")
        # Отображение графика
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Функция обновления графика после расчета для нового графа
        def update_plot():
            ax.clear()
            ax.set_title("Зависимость t от n-узлов")
            ax.set_xlabel("Количество узлов")
            ax.set_ylabel("Время (сек)")
            # Сортировка для построения линии
            pairs = sorted(zip(nodes_list, times_list), key=lambda x: x[1])
            x_sorted = [p[0] for p in pairs]
            y_sorted = [p[1] for p in pairs]
            # Точки
            ax.scatter(nodes_list, times_list, marker='o', color='blue')
            # Линия
            ax.plot(x_sorted, y_sorted, color='red')

            canvas.draw()


        def find_scc():
            try:
                steps_area.delete("1.0", tk.END)
                directed = is_directed_var.get()
                method = input_method_var.get()
                time_label.config(text="")
                if method == "manual":
                    raw_data = input_field.get("1.0", tk.END).strip()
                    if not raw_data:
                        raise ValueError("Поле ввода пустое! Введите граф в указанном формате.")
                    graph = parse_adjacency_list(raw_data, directed=directed)
                    
                    # Количество узлов для графика
                    num_nodes = len(graph.keys())
                    output_area.delete("1.0", tk.END)
                else:
                    num_nodes_val = num_nodes_entry.get()
                    edge_prob_val = edge_prob_entry.get()
                    if not num_nodes_val or not edge_prob_val:
                        raise ValueError("Пожалуйста, укажите количество узлов и вероятность ребра.")
                    try:
                        num_nodes = int(num_nodes_val)
                        edge_prob = float(edge_prob_val)
                        if num_nodes <= 0 or not (0 <= edge_prob <= 1):
                            raise ValueError
                    except ValueError:
                        raise ValueError("Некорректные значения для количества узлов или вероятности ребра.")
                    graph = generate_random_graph(num_nodes, edge_prob, directed=directed)
                    raw_data = graph_to_adjacency_list(graph)
                    
                    output_area.delete("1.0", tk.END)
                    # Отображаем сгенерированный граф в поле вывода
                    output_area.insert(tk.END, "Сгенерированный граф (список смежности):\n")
                    output_area.insert(tk.END, raw_data + "\n\n")

                # Запускаем таймер
                start_time = time.time()

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

                def find_connected_components(graph):
                    visited = set()
                    components = []

                    def dfs_cc(node, component):
                        visited.add(node)
                        component.append(node)
                        steps_area.insert(tk.END, f"Обходим вершину {node}\n")
                        for neighbor in graph[node]:
                            if neighbor not in visited:
                                steps_area.insert(tk.END, f"  Заходим в соседнюю вершину {neighbor}\n")
                                dfs_cc(neighbor, component)

                    for node in graph:
                        if node not in visited:
                            steps_area.insert(tk.END, f"Начинаем новый обход с вершины {node}\n")
                            component = []
                            dfs_cc(node, component)
                            components.append(component)
                            steps_area.insert(tk.END, f"Найдена компонента связности: {component}\n")

                    return components

                # Если был выбран случайный ввод, парсим граф из сгенерированных данных
                if method == "random":
                    graph = parse_adjacency_list(raw_data, directed=directed)

                if directed:
                    sccs = kosaraju(graph)
                    # Останавливаем таймер
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if method == "manual":
                        output_area.insert(tk.END, "Компоненты сильной связности:\n")
                    for i, component in enumerate(sccs, 1):
                        output_area.insert(tk.END, f"Компонента {i}: {component}\n")
                else:
                    components = find_connected_components(graph)
                    # Останавливаем таймер
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    if method == "manual":
                        output_area.insert(tk.END, "Компоненты связности:\n")
                    for i, component in enumerate(components, 1):
                        output_area.insert(tk.END, f"Компонента {i}: {component}\n")

                # Вывод времени работы алгоритма
                time_label.config(text=f"{elapsed_time:.6f} секунд")
                # Обновление графика
                nodes_list.append(num_nodes)
                times_list.append(elapsed_time)
                update_plot()

            except ValueError as ve:
                messagebox.showerror("Ошибка ввода", str(ve))
            except Exception as e:
                messagebox.showerror("Ошибка", f"Произошла ошибка при обработке графа:\n{e}")

        tk.Button(right_frame, text="Выполнить алгоритм", command=find_scc, font=("Arial", 12)).pack(pady=10)
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
        "Название задания: Реализация алгоритма выделения компонент связности графа.\n\n"
        "Описание алгоритма:\n"
        "Для ориентированного графа используется алгоритм Косарайю для выделения компонент сильной связности.\n"
        "Для неориентированного графа используется поиск в глубину (DFS) для нахождения компонент связности.\n\n"
        "Программа поддерживает ручной ввод или случайную генерацию графа.\n"
        "Добавлен график зависимости времени выполнения от количества узлов."
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
