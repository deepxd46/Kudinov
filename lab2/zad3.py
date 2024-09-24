def smena_diagonal(matrix):
    a = len(matrix)

    for i in range(a):
        matrix[i][i], matrix[i][a - 1 - i] = matrix[i][a - 1 - i], matrix[i][i]

    return matrix

matrix = [
    [1, 2 ,3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = smena_diagonal(matrix)

for row in new_matrix:
    print(row)