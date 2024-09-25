spisok = [1,2,3,4,5,6,7,8,9,10]

srednee = sum(spisok)/len(spisok)

bolshe = [x for x in spisok if x > srednee]
menshe = [x for x in spisok if x <= srednee]

print('Элементы большие среднего', bolshe)
print('Элементы меньше среднего', menshe)

