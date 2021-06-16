"""
Создать текстовый файл test_file.txt,
заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор»
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

with open('test_file.txt', 'w') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')
    print(f'Кодировка по умолчанию {f.encoding=}')


with open('test_file.txt', 'r', encoding='utf-8') as t_f:
    for row in t_f:
        print(row)

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte
# Кодировка по умолчанию f.encoding='cp1251'
# Гуглил и нормального ответа не нашёл
