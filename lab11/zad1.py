import os

def create_sample_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("10\n20\n30\n40\n50\n")
        print(f"Файл {filename} создан с примерными данными.")


def create_linked_list(numbers):
    if not numbers:
        return None
    head = {"value": numbers[0], "next": None}
    current = head
    for number in numbers[1:]:
        new_node = {"value": number, "next": None}
        current["next"] = new_node
        current = new_node
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current["value"])
        current = current["next"]
    return result


def linear_search_linked_list(head, target):
    current = head
    while current:
        if current["value"] == target:
            return True
        current = current["next"]
    return False


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def read_numbers_from_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return [int(line.strip()) for line in lines if line.strip().isdigit()]
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def write_results_to_file(filename, linked_list, target, linear_result, binary_result):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Числа в файле (из связного списка):\n")
        current = linked_list
        while current:
            file.write(f"{current['value']}\n")
            current = current["next"]

        file.write("\nРезультаты поиска:\n")
        file.write(f"Искомое число: {target}\n")
        file.write(f"Линейный поиск: {'Найден' if linear_result else 'Не найден'}\n")
        file.write(f"Бинарный поиск: {'Найден' if binary_result else 'Не найден'}\n")


if __name__ == "__main__":
    filename = "numbers.txt"

    create_sample_file(filename)

    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("Файл пуст или содержит некорректные данные.")
    else:
        linked_list = create_linked_list(numbers)

        target_number = 50  


        linear_result = linear_search_linked_list(linked_list, target_number)

        sorted_list = sorted(numbers)
        binary_result = binary_search(sorted_list, target_number)

        write_results_to_file(filename, linked_list, target_number, linear_result, binary_result)

        print(f"Результаты записаны в файл {filename}.")
