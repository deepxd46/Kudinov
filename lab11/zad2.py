def binary_search(arr, key):
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
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    # Пример
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    key = 10

    is_found = binary_search(arr, key)
    if is_found:
        print(f"Элемент {key} найден в массиве.")
    else:
        print(f"Элемент {key} не найден в массиве.")

    insert_position = find_insert_position(arr, key)
    print(f"Элемент {key} следует вставить на позицию {insert_position}.")
