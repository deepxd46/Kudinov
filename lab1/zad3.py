spisok = [1,2,3,4,5,6,7,8,9,10]

srednee = sum(spisok)/len(spisok)

bolshie = [x for x in spisok if x > srednee]
menshie = [x for x in spisok if x <= srednee]

print('Элементы большие среднего', bolshie)
print('Элементы меньше среднего', menshie)

