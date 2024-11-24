def read_numbers_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(map(int, file.read().split()))

def write_results_to_file(filename, results):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(results))

def linear_search(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index
    return -1

def binary_search(numbers, target):
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
    input_file = 'D:\GITHUB\Kudinov\lab11\input.txt'  
    output_file = 'D:\GITHUB\Kudinov\lab11\output.txt'  
    target = int(input("Введите число для поиска: "))  

    
    numbers = read_numbers_from_file(input_file)

    
    linear_result = linear_search(numbers, target)
    linear_message = (f"Линейный поиск: число {target} найдено на позиции {linear_result}"
                      if linear_result != -1 else f"Линейный поиск: число {target} не найдено")

    
    numbers.sort()  
    binary_result = binary_search(numbers, target)
    binary_message = (f"Бинарный поиск: число {target} найдено на позиции {binary_result}"
                      if binary_result != -1 else f"Бинарный поиск: число {target} не найдено")

    
    write_results_to_file(output_file, [linear_message, binary_message])
    print("Результаты поиска записаны в файл:", output_file)

if __name__ == "__main__":
    main()
