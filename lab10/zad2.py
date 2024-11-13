def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers

def write_numbers(file_path, numbers):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, numbers)))

def counting_sort_asc(arr):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    count = [0] * (max_val - min_val + 1)
    
    for num in arr:
        count[num - min_val] += 1
    print(f"Промежуточное состояние счётчика: {count}")
    
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i + min_val] * cnt)
        if cnt > 0:
            print(f"Добавление числа {i + min_val} в отсортированный массив: {sorted_arr}")
    return sorted_arr

if __name__ == "__main__":
    input_file = r'D:\GITHUB\Kudinov\lab10\3.txt'
    output_file = r'D:\GITHUB\Kudinov\lab10\4.txt'

    numbers = read_numbers(input_file)
    print(f"Исходный массив: {numbers}")
    sorted_numbers = counting_sort_asc(numbers)
    write_numbers(output_file, sorted_numbers)
    print(f"Сортировка подсчетом по возрастанию завершена. Результат записан в {output_file}")
