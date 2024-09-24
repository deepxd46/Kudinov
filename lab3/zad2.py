def vostanovlenie(verx_trey, N):
    matrix = [[0] * N for _ in range(N)]

    index = 0 

    for i in range(N):
        for j in range(i, N):
            matrix[i][j] = verx_trey[index]
            matrix[j][i] = verx_trey[index]
            index += 1 
        
    return matrix

N = 3
verx_trey = [1, 2, 3, 4, 5, 6]

simitriya = vostanovlenie(verx_trey, N)

for row in simitriya:
    print(row)