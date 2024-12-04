def binary_search(arr, key):
    """Возвращает True, если элемент key найден в отсортированном массиве arr, иначе False."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_insert_position(arr, key):
    """Возвращает индекс, куда нужно вставить key в отсортированный массив arr."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    # Пример отсортированного массива
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    # Элемент для поиска и вставки
    key = 10

    # 1. Проверим, есть ли элемент key в массиве с помощью бинарного поиска
    is_found = binary_search(arr, key)
    if is_found:
        print(f"Элемент {key} найден в массиве.")
    else:
        print(f"Элемент {key} не найден в массиве.")

    # 2. Определим, на какое место нужно вставить key, чтобы сохранить упорядоченность
    insert_position = find_insert_position(arr, key)
    print(f"Элемент {key} следует вставить на позицию {insert_position}.")
