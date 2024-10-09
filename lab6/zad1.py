file_name = r'D:\GITHUB\Kudinov\lab6\textfile.txt'

file = open(file_name, 'r+', encoding='utf-8')
try:
    lines = file.readlines()
    
    original_string = lines[0].strip()
    
    new_string = ''.join(original_string[i] for i in range(len(original_string)) if i % 2 == 0)

    file.seek(0, 2)
    file.write(new_string + '\n')
finally:
    file.close()
