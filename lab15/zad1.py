import math

# Определяем функции для каждого оператора
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Division by zero")

def square_root(a):
    return math.sqrt(a)

def exponentiate(a, b):
    return pow(a, b)

# Словарь для сопоставления символов операторов с соответствующими им функциями
operator_functions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'sqrt': square_root,
    'exp': exponentiate
}

def main():
    print("Simple Calculator")
    current_result = 0
    
    while True:
        try:
            # Выведите текущий результат, если он не равен нулю
            if current_result != 0:
                print(f"Current Result: {current_result}")
            
            # Получение пользовательского ввода для первого числа или оператора
            if current_result == 0:
                current_result = float(input("Enter a number: "))

            # Убедимся, что пользователь вводит все через пробел
            operator_input = input("Enter an operator (+, -, *, /): ").strip().lower()
            operator = operator_input[0]  # Извлекаем первый символ, в качестве оператора
            
            # Обработка случая, когда оператор не введен или введен только пробел
            if not operator:
                raise ValueError("Invalid operator. Please enter +, -, *, /.")
            
            num2 = float(input("Enter second number: "))
            
            # Выполняем вычисление, смотря на выбранный оператор
            if operator in operator_functions:
                result = operator_functions[operator](current_result, num2)
                current_result = result
            else:
                raise ValueError("Invalid operator. Please enter +, -, *, /, sqrt, or exp.")
            
            # Выведение результата
            print(f"Current Result: {current_result}")
            
        except ValueError as e:
            print(e)
        
        # Спросите пользователя, хочет ли он выполнить еще одно вычисление
        # again = input("Хотите ли вы выполнить еще один расчет? (yes/no): ").strip().lower()
        # if again != 'yes':
        #     break

if __name__ == "__main__":
    main()