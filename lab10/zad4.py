def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers

def write_numbers(file_path, numbers):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, numbers)))

def merge(left, right):
    result = []
    print(f"Слияние: левый={left}, правый={right}")
    while left and right:
        if left[0] > right[0]:  
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        print(f"Промежуточный результат слияния: {result}")
    result.extend(left or right)
    print(f"Результат после завершения слияния: {result}")
    return result

def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])
    print(f"Разделение: левый={left}, правый={right}")
    return merge(left, right)

if __name__ == "__main__":
    input_file = r'D:\GITHUB\Kudinov\lab10\7.txt'
    output_file = r'D:\GITHUB\Kudinov\lab10\8.txt'

    numbers = read_numbers(input_file)
    print(f"Исходный массив: {numbers}")
    sorted_numbers = merge_sort_desc(numbers)
    write_numbers(output_file, sorted_numbers)
    print(f"Сортировка слиянием по убыванию завершена. Результат записан в {output_file}")
