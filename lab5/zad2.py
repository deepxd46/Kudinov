def vvod():
    n = int(input("Ввкдите количество элементов: "))
    massiv = []

    for i in range(n):
        element = int(input("Введите элемент (i + 1): "))
        massiv.append(element)

    return massiv

def minimal(massiv):
    minimal_element = None

    for element in massiv:
        if element > 0 and element % 10 == 5:
            if minimal_element is None or element < minimal_element:
                minimal_element = element

    return minimal_element

def konech():
    massiv = vvod()

    result = minimal(massiv)
    if result is not None:
        print("Минимальный положительный элемент, оканчивающийся на 5: ", result)
    else:
        print("Нет положительных элементов, оканчивающихся на 5")

konech()


