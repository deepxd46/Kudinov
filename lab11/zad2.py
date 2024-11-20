def binary_search(numbers, key):
    """
    Проверяет, есть ли элемент `key` в массиве `numbers`.
    Возвращает True, если найден, иначе False.
    """
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == key:
            return True
        elif numbers[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_insert_position(numbers, key):
    """
    Находит индекс, куда нужно вставить элемент `key`, чтобы
    сохранить упорядоченность массива `numbers`.
    """
    left, right = 0, len(numbers)
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    input_file = 'input.txt'  # Файл с исходным списком чисел
    output_file = 'output.txt'  # Файл для записи результатов

    # Чтение массива из файла
    with open(input_file, 'r') as file:
        numbers = list(map(int, file.read().split()))

    # Сортировка массива
    numbers.sort()

    # Запрос ключа для поиска
    key = int(input("Введите ключ для поиска: "))

    # Бинарный поиск
    is_found = binary_search(numbers, key)
    insert_position = find_insert_position(numbers, key)

    # Формирование ответа
    search_result = (f"Элемент {key} найден в массиве." 
                     if is_found else f"Элемент {key} не найден в массиве.")
    insert_result = f"Элемент {key} следует вставить на позицию {insert_position}."

    # Запись в файл
    with open(output_file, 'w') as file:
        file.write(search_result + '\n')
        file.write(insert_result + '\n')

    # Вывод результата
    print(search_result)
    print(insert_result)
    print(f"Результаты записаны в файл: {output_file}")

if __name__ == "__main__":
    main()
