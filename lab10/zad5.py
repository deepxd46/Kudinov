import os
import heapq

def sort_and_split_file(input_file, chunk_size=10):
    sub_files = []
    with open(input_file, 'r') as file:
        numbers = []
        for line in file:
            numbers.extend(map(int, line.split()))
            while len(numbers) >= chunk_size:
                chunk = sorted(numbers[:chunk_size])
                sub_file_name = f'sorted_chunk_{len(sub_files)}.txt'
                with open(sub_file_name, 'w') as sub_file:
                    sub_file.write('\n'.join(map(str, chunk)))
                print(f"Создан отсортированный файл-чунк: {sub_file_name} с содержимым: {chunk}")
                sub_files.append(sub_file_name)
                numbers = numbers[chunk_size:]

        if numbers:
            chunk = sorted(numbers)
            sub_file_name = f'sorted_chunk_{len(sub_files)}.txt'
            with open(sub_file_name, 'w') as sub_file:
                sub_file.write('\n'.join(map(str, chunk)))
            print(f"Создан отсортированный файл-чунк: {sub_file_name} с оставшимися данными: {chunk}")
            sub_files.append(sub_file_name)

    return sub_files

def merge_sorted_files(sorted_files, output_file):
    min_heap = []
    file_iters = [open(f, 'r') for f in sorted_files]

    for i, f in enumerate(file_iters):
        number = f.readline().strip()
        if number:
            heapq.heappush(min_heap, (int(number), i))
    print(f"Начальное состояние кучи: {min_heap}")

    with open(output_file, 'w') as outfile:
        while min_heap:
            smallest, file_index = heapq.heappop(min_heap)
            outfile.write(f"{smallest}\n")
            print(f"Запись числа {smallest} в выходной файл. Текущее состояние кучи: {min_heap}")
            next_number = file_iters[file_index].readline().strip()
            if next_number:
                heapq.heappush(min_heap, (int(next_number), file_index))
                print(f"Добавлено число {next_number} из файла {sorted_files[file_index]} в кучу. Обновленное состояние кучи: {min_heap}")

    for f in file_iters:
        f.close()

def external_sort(input_file, output_file, chunk_size=10):
    sorted_files = sort_and_split_file(input_file, chunk_size)
    merge_sorted_files(sorted_files, output_file)

    for f in sorted_files:
        os.remove(f)
        print(f"Удален временный файл-чунк: {f}")

if __name__ == "__main__":
    input_file = r'D:\GITHUB\Kudinov\lab10\9.txt'  
    output_file = r'D:\GITHUB\Kudinov\lab10\10.txt'  
    external_sort(input_file, output_file)
    print(f"Внешняя сортировка завершена. Результат записан в {output_file}.")
