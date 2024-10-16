import csv

def create_payroll_txt(file):
    with open(file, mode='w', encoding='utf-8') as f:
        f.write("ФИО;Подразделение;Рабочие дни;Зарплата\n")
        f.write("Иванов Иван Иванович;001;20;50000\n")
        f.write("Петров Петр Петрович;002;22;55000\n")
        f.write("Сидорова Анна Васильевна;001;19;48000\n")
        f.write("Кузнецов Олег Дмитриевич;003;21;52000\n")
        f.write("Васильева Наталья Сергеевна;002;23;60000\n")

def read_payroll_txt(file):
    payroll_dict = {}
    with open(file, mode='r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
        for line in lines:
            fio, department, work_days, salary = line.strip().split(';')
            payroll_dict[fio] = {
                'Подразделение': department,
                'Рабочие дни': int(work_days),
                'Зарплата': int(salary)
            }
    return payroll_dict

def search_by_surname(payroll_dict, surname):
    return {fio: data for fio, data in payroll_dict.items() if surname.lower() in fio.lower()}

def search_by_department(payroll_dict, department):
    return {fio: data for fio, data in payroll_dict.items() if data['Подразделение'] == department}

def search_by_salary(payroll_dict, salary):
    return {fio: data for fio, data in payroll_dict.items() if data['Зарплата'] == salary}

def search_by_workdays_range(payroll_dict, min_days, max_days):
    return {fio: data for fio, data in payroll_dict.items() if min_days <= data['Рабочие дни'] <= max_days}

def total_salary_by_department(payroll_dict, department):
    total_salary = sum(data['Зарплата'] for data in payroll_dict.values() if data['Подразделение'] == department)
    return total_salary

def choose_search_option(payroll_dict):
    print("Выберите опцию для поиска:")
    print("1. Поиск по фамилии")
    print("2. Поиск по подразделению")
    print("3. Поиск по зарплате")
    print("4. Поиск по диапазону рабочих дней")
    print("5. Общая сумма выплат по подразделению")
    
    choice = input("Введите номер опции: ")

    if choice == '1':
        surname = input("Введите фамилию для поиска: ")
        results = search_by_surname(payroll_dict, surname)
        print("Результаты поиска по фамилии:", results)
        
    elif choice == '2':
        department = input("Введите номер подразделения: ")
        results = search_by_department(payroll_dict, department)
        print("Результаты поиска по подразделению:", results)
        
    elif choice == '3':
        salary = int(input("Введите зарплату для поиска: "))
        results = search_by_salary(payroll_dict, salary)
        print("Результаты поиска по зарплате:", results)
        
    elif choice == '4':
        min_days = int(input("Введите минимальное количество рабочих дней: "))
        max_days = int(input("Введите максимальное количество рабочих дней: "))
        results = search_by_workdays_range(payroll_dict, min_days, max_days)
        print("Результаты поиска по диапазону рабочих дней:", results)
        
    elif choice == '5':
        department = input("Введите номер подразделения для расчёта общей суммы выплат: ")
        total_salary = total_salary_by_department(payroll_dict, department)
        print(f"Общая сумма выплат для подразделения {department}: {total_salary}")
        
    else:
        print("Неверный выбор!")

txt_filename = "payroll_data_example.txt"
create_payroll_txt(txt_filename)
payroll_dict = read_payroll_txt(txt_filename)

choose_search_option(payroll_dict)
