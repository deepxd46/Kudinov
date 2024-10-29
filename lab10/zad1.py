def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers

def write_numbers(file_path, numbers):
    with open(file_path, 'w') as file:
        file.write(" ".join(map(str, numbers)))

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    input_file = r'D:\GITHUB\Kudinov\lab10\1.txt'
    output_file = r'D:\GITHUB\Kudinov\lab10\2.txt'

    numbers = read_numbers(input_file)
    sorted_numbers = bubble_sort_asc(numbers)
    write_numbers(output_file, sorted_numbers)
    print(f"Сортировка пузырьком по возрастанию завершена. Результат записан в {output_file}")
