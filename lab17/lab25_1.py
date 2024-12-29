def read_graph_data_from_file(file_path):
    # Инициализируем переменные для количества вершин и ребер
    num_vertices = 0
    num_edges = 0

    # Открываем файл для чтения
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Убираем возможные лишние символы в начале и конце строки
            if not line:  # Пропускаем пустые строки
                continue

            parts = line.split()
            if len(parts) == 4 and parts[0] == 'num_vertices' and parts[2] == 'num_edges':
                num_vertices = int(parts[1])
                num_edges = int(parts[3])
                break

    # Создаем матрицу смежности
    adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Читаем остальные строки файла для заполнения матрицы смежности
    with open(file_path, 'r') as file:
        next(file)  # Пропускаем заголовок с количеством вершин и ребер

        for line in file:
            parts = line.split()
            if len(parts) == 3 and parts[0] == 'edge':
                u = int(parts[1]) - 1
                v = int(parts[2]) - 1
                adjacency_matrix[u][v] = 1
                adjacency_matrix[v][u] = 1

    return num_vertices, num_edges, adjacency_matrix

# Пример использования программы
file_path = 'D:\\GITHUB\\Kudinov\\lab17\\graph_data.txt'
num_vertices, num_edges, adjacency_matrix = read_graph_data_from_file(file_path)

print(f"Количество вершин: {num_vertices}")
print(f"Количество ребер: {num_edges}")

# Вывод матрицы смежности
print("-------------------")
print("Матрица Смежности:")
for row in adjacency_matrix:
    print(row)