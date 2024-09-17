a = int(input('Введите количество строк в матрице a: '))
b = int(input('Введите количество столбцов в матрице b: '))

matricha = []
print('Введите элементы матрицы построчно: ')
for i in range(a):
    row = list(map(int, input().split()))
    matricha.append(row)

otrich_elementi = []

for row in matricha:
    otr_sum = sum(x for x in row if x < 0)
    otrich_elementi.append(otr_sum)

print('Массив сумм отрицательных элементов каждой строки: ', otrich_elementi)
