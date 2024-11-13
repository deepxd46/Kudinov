def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers

def write_numbers(file_path, numbers):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, numbers)))

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"Начинается вставка элемента {key} на позицию {i}")
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Промежуточный массив: {arr}")
        arr[j + 1] = key
        print(f"После вставки {key}: {arr}")
    return arr

if __name__ == "__main__":
    input_file = r'D:\GITHUB\Kudinov\lab10\5.txt'
    output_file = r'D:\GITHUB\Kudinov\lab10\6.txt'

    numbers = read_numbers(input_file)
    print(f"Исходный массив: {numbers}")
    sorted_numbers = insertion_sort_desc(numbers)
    write_numbers(output_file, sorted_numbers)
    print(f"Сортировка вставками по убыванию завершена. Результат записан в {output_file}")
