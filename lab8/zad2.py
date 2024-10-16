def count_squares(a, b):
    if a == 0 or b == 0:
        return 0
    square_side = min(a, b)
    if a >= b:
        return 1 + count_squares(a - square_side, b)
    else:
        return 1 + count_squares(a, b - square_side)

a = 5
b = 3
num_squares = count_squares(a, b)
print(f"Количество квадратов, на которые можно разрезать прямоугольник {a}x{b}: {num_squares}")
