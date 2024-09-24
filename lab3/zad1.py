def craft(n):
    matrix = [[0] * n for _ in range(n)]

    verx, niz, levya, pravaya = 0, n - 1, 0, n - 1
    a = 1

    while verx <= niz and levya <= pravaya:
        for i in range(levya, pravaya + 1):
            matrix[verx][i] = a
            a += 1 
        verx += 1

        for i in range(verx, niz + 1):
            matrix[i][pravaya] = a
            a += 1
        pravaya -= 1

        for i in range(pravaya, levya - 1, -1):
            matrix[niz][i] = a
            a += 1
        niz -= 1

        for i in range(niz, verx - 1, -1):
            matrix[i][levya] = a
            a += 1
        levya += 1

    return matrix

N = 5
new_matrix = craft(N)

for row in new_matrix:
    print(row)