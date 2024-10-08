import re

input_file_name = r'D:\GITHUB\Kudinov\lab6\text2.txt'
output_file_name = r'D:\GITHUB\Kudinov\lab6\result.txt'

with open(input_file_name, 'r', encoding='utf-8') as input_file:
    data = input_file.read()
    
    words = re.findall(r'\b\w+\b', data)
    word_count = len(words)
    
    digit_count = sum(char.isdigit() for char in data)

with open(output_file_name, 'w', encoding='utf-8') as output_file:
    output_file.write(f'Количество слов: {word_count}\n')
    output_file.write(f'Количество цифр: {digit_count}\n')
