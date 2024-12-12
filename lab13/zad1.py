import random
import string

def levenshtein_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    

    for i in range(len1 + 1):
        dp[i][0] = i 
    for j in range(len2 + 1):
        dp[0][j] = j  
    
    # Заполнение таблицы
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  
            else:
                dp[i][j] = min(dp[i - 1][j - 1],  
                               dp[i - 1][j],      
                               dp[i][j - 1]) + 1 
    
    return dp[len1][len2]

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def main():
    print("Выберите вариант:")
    print("1. Ввести строки вручную")
    print("2. Сгенерировать случайные строки")

    choice = input("Введите 1 или 2: ").strip()

    if choice == "1":
        str1 = input("Введите первую строку: ").strip()
        str2 = input("Введите вторую строку: ").strip()
    elif choice == "2":
        len1 = random.randint(1, 10) 
        len2 = random.randint(1, 10)  
        str1 = generate_random_string(len1)
        str2 = generate_random_string(len2)
        print(f"Сгенерированные строки:\nstr1 = {str1}\nstr2 = {str2}")
    else:
        print("Неверный выбор, попробуйте снова.")
        return

    print(f"Расстояние Левенштейна между строками '{str1}' и '{str2}': {levenshtein_distance(str1, str2)}")


main()
