
def crt():
    n = int(input("введите число: "))
    arr = [0] * n
    for i in range(n):
        arr[i] = [0] * n
    for i in range(n):
        for j in range(n):
            temp = i
            while temp != 0:
                arr[i][j] = n - temp
                temp -= 1
            else:
                arr[i][j] = n
                break
    return arr


print(crt())