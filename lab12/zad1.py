import random
import string

def create_hash_table(size=10):
    """Создает хэш-таблицу с заданным размером."""
    return [[] for _ in range(size)]


def _hash(key, size):
    """Хэш-функция для вычисления индекса по ключу."""
    return hash(key) % size


def add(hash_table, key, value):
    """Добавляет элемент в хэш-таблицу с обработкой коллизий."""
    index = _hash(key, len(hash_table))
    # Проверяем, есть ли уже такой ключ в соответствующем списке
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value  # Если ключ найден, обновляем значение
            return
    # Если ключ не найден, добавляем новый элемент
    hash_table[index].append([key, value])


def remove(hash_table, key):
    """Удаляет элемент из хэш-таблицы."""
    index = _hash(key, len(hash_table))
    for i, pair in enumerate(hash_table[index]):
        if pair[0] == key:
            del hash_table[index][i]
            return True
    return False  # Если элемент не найден


def search(hash_table, key):
    """Ищет элемент в хэш-таблице и возвращает его значение, если найден."""
    index = _hash(key, len(hash_table))
    for pair in hash_table[index]:
        if pair[0] == key:
            return pair[1]
    return None  # Если элемент не найден


def display(hash_table):
    """Выводит хэш-таблицу на экран."""
    for i, bucket in enumerate(hash_table):
        if bucket:
            print(f"Индекс {i}: {bucket}")
        else:
            print(f"Индекс {i}: Пусто")


def random_string(length=5):
    """Генерирует случайную строку длиной length, состоящую из букв и цифр."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


def random_int(min_value=1, max_value=100):
    """Генерирует случайное целое число."""
    return random.randint(min_value, max_value)


# Пример использования хэш-таблицы с рандомным вводом

if __name__ == "__main__":
    # Создаем хэш-таблицу
    size = 10
    hash_table = create_hash_table(size)

    # Генерация случайных ключей и значений
    for _ in range(10):  # Добавим 10 случайных элементов
        key = random_string(random.randint(3, 8))  # Случайная строка длиной от 3 до 8 символов
        value = random_int(1, 100)  # Случайное значение от 1 до 100
        add(hash_table, key, value)
        print(f"Добавлен элемент: {key} = {value}")

    # Печать хэш-таблицы
    print("\nТекущая хэш-таблица:")
    display(hash_table)

    # Случайный поиск элемента
    search_key = random_string(random.randint(3, 8))
    print(f"\nПоиск элемента с ключом '{search_key}': {search(hash_table, search_key)}")

    # Случайное удаление элемента
    remove_key = random_string(random.randint(3, 8))
    removed = remove(hash_table, remove_key)
    print(f"\nУдаление элемента с ключом '{remove_key}': {removed}")

    # Печать таблицы после изменений
    print("\nХэш-таблица после изменений:")
    display(hash_table)
