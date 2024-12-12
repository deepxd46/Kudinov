class Heap:
    def __init__(self, data=None):
        self.data = data if data is not None else []
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        smallest_index = index

        if (left_child_index < len(self.data)) and (self.data[left_child_index] < self.data[smallest_index]):
            smallest_index = left_child_index

        if (right_child_index < len(self.data)) and (self.data[right_child_index] < self.data[smallest_index]):
            smallest_index = right_child_index

        if smallest_index != index:
            self.data[index], self.data[smallest_index] = self.data[smallest_index], self.data[index]
            self._heapify_down(smallest_index)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[parent_index] > self.data[index]:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            else:
                break
            index = parent_index

    def insert(self, element):
        self.data.append(element)
        self._heapify_up(len(self.data) - 1)

    def extract_min(self):
        if len(self.data) == 0:
            return None
        min_element = self.data[0]
        last_element = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = last_element
            self._heapify_down(0)
        return min_element

    def build_heap(self, data):
        self.data = data[:]
        for i in range(len(data) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def merge_heaps(self, other_heap):
        if not isinstance(other_heap, Heap):
            raise ValueError("Вторая куча должна быть экземпляром класса Heap")
        
        merged_data = self.data + other_heap.data
        self.build_heap(merged_data)

    def heap_sort(self):
        sorted_data = []
        while len(self.data) > 0:
            sorted_data.append(self.extract_min())
        return sorted_data

# Пример использования
if __name__ == "__main__":
    # Создание кучи
    min_heap = Heap()
    
    # Добавление элементов
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(4)
    min_heap.insert(1)
    min_heap.insert(5)
    min_heap.insert(9)

    print("Куча после добавления:", min_heap.data)  # [1, 1, 3, 4, 5, 9]

    # Удаление минимального элемента
    min_element = min_heap.extract_min()
    print("Удаленный минимальный элемент:", min_element)  # 1

    # Построение кучи из массива
    heap_array = [3, 1, 4, 1, 5, 9]
    min_heap.build_heap(heap_array)
    print("Куча после построения:", min_heap.data)  # [1, 1, 3, 4, 5, 9]

    # Объединение двух куч
    max_heap = Heap([2, 6, 8])
    min_heap.merge_heaps(max_heap)
    print("Куча после объединения:", min_heap.data)  # [1, 1, 3, 4, 5, 9, 2, 6, 8]

    # Пирамидальная сортировка
    sorted_array = min_heap.heap_sort()
    print("Отсортированный массив:", sorted_array)