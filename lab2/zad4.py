def summirovanie(matrix):
    N = len(matrix)
    M = len(matrix[0])

    a = 0

    for j in range(M):
        a += matrix[0][j]
        a += matrix[N - 1][j]

    for i in range(1, N - 1):
        a += matrix[i][0]
        a += matrix[i][M - 1]

    return a

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = summirovanie(matrix)
print('Сумма элементов по контуру массива:', result)