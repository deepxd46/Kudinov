def otrich_elementi(row):
    return sum([x for x in row if x < 0])

def summa(matrix):
    otrich_summ = [otrich_elementi(row) for row in matrix]
    return otrich_summ

x = [
    [1, -22, -10],
    [22, -55, 0],
    [0, 10, 255]    
]

result = summa(x)
print(result)