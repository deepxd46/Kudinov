def extended_gcd(a, b):
    # Базовый случай: если b == 0, то НОД(a, 0) == a и (x, y) = (1, 0)
    if b == 0:
        return a, 1, 0
    else:
        # Рекурсивный вызов алгоритма Евклида
        gcd, x1, y1 = extended_gcd(b, a % b)
        # Вычисляем x и y
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Пример использования:
a = 252
b = 198
gcd, x, y = extended_gcd(a, b)

print(f"НОД({a}, {b}) = {gcd}")
print(f"Коэффициенты: x = {x}, y = {y}")
print(f"Проверка: {a} * {x} + {b} * {y} = {gcd}")
