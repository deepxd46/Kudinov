from math import sqrt
from prettytable import PrettyTable


beg = int(input('Введите начало: '))
end = int(input('Введите конец: '))
h = float(input('Введите шаг для аргумента: '))


def function(x):
    while x < -9:
        return 'Функция не существует'
    while -9 <= x <= -6:
        return -2*x-19
    while -6 <= x <= -1:
        return 9/5*x + 19/5
    while -1 <= x <= 2:
        return 1/3*x + 7/3
    while 2 <= x <= 7:
        return 3
    while 7 <= x <= 9:
        return ((1 - (x-8) ** 2) ** (1/2)) + 3
    while x > 9:
        return 'Функции не существует'


tabel = PrettyTable()
tabel.field_names = ['Аргумент', 'Значение']
while beg <= end:
    tabel.add_row([beg, function(beg)])
    beg += h
print(tabel)