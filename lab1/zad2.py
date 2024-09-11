def proverka(spisok):
    x_spisok = []
    for x in spisok:
        if x != 0:
            x_spisok.append(x)
    return x_spisok

list = [1,2,45,6,6,7,78,0]
y_spisok = proverka(list)
print(y_spisok)