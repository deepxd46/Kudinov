import numpy as np 

x = int(input('Введите размерность матрицы x: '))

matricha = np.random.randint(1, 100, (x, x))
print('Матрица matricha:')
print(matricha)

sum_diagonal = 0 

for i in range(x):
    if matricha[i, x - 1 - i] % 5 == 0:
        sum_diagonal += matricha[i, x - 1 - i]

print('Сумма чисел побочной диагонали, чисел кратых 5:', sum_diagonal)