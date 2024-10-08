def main():
    my_name = "Иван"
    my_surname = "Иванов"

    with open(r'D:\GITHUB\Kudinov\lab6\text1.txt', 'r', encoding='utf-8') as file:
        students = [line.strip() for line in file.readlines()]

    count_with_name = sum(1 for student in students if student.split()[1] == my_name)

    same_surnames = [student for student in students if student.split()[0] == my_surname]

    with open('report.txt', 'w', encoding='utf-8') as report_file:
        report_file.write(f"Отчет составлен {my_surname} {my_name}.\n")
        report_file.write(f"Количество студентов в группе с именем {my_name} ‒ {count_with_name} студента.\n")
        
        if same_surnames:
            report_file.write(f"В группе есть однофамилец ‒ {', '.join(same_surnames)}.\n")
        else:
            report_file.write("В группе нет однофамильцев.\n")

if __name__ == "__main__":
    main()
