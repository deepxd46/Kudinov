def read_numbers_from_file(filename):
    """Читает числа из текстового файла и возвращает их как список."""
    with open(filename, 'r', encoding='utf-8') as file:
        return list(map(int, file.read().split()))

def write_results_to_file(filename, results):
    """Записывает результаты поиска в текстовый файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(results))

def linear_search(numbers, target):
    """Реализация линейного поиска."""
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return -1

def binary_search(numbers, target):
    """Реализация бинарного поиска. Список должен быть отсортирован."""
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    input_file = 'D:\GITHUB\Kudinov\lab11\input.txt'  # Файл с исходным списком чисел
    output_file = 'D:\GITHUB\Kudinov\lab11\output.txt'  # Файл для записи результатов
    target = int(input("Введите число для поиска: "))  # Число для поиска

    # Чтение списка чисел
    numbers = read_numbers_from_file(input_file)

    # Линейный поиск
    linear_result = linear_search(numbers, target)
    linear_message = (f"Линейный поиск: число {target} найдено на позиции {linear_result}"
                      if linear_result != -1 else f"Линейный поиск: число {target} не найдено")

    # Бинарный поиск
    numbers.sort()  # Сортируем список для бинарного поиска
    binary_result = binary_search(numbers, target)
    binary_message = (f"Бинарный поиск: число {target} найдено на позиции {binary_result}"
                      if binary_result != -1 else f"Бинарный поиск: число {target} не найдено")

    # Запись результатов
    write_results_to_file(output_file, [linear_message, binary_message])
    print("Результаты поиска записаны в файл:", output_file)

if __name__ == "__main__":
    main()
