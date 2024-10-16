def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

a = 352
b = 228
gcd, x, y = extended_gcd(a, b)

print(f"НОД({a}, {b}) = {gcd}")
print(f"Коэффициенты: x = {x}, y = {y}")
print(f"Проверка: {a} * {x} + {b} * {y} = {gcd}")
