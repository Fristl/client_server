"""
Создать текстовый файл test_file.txt,
заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор»
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import chardet

words = ['сетевое программирование\n', 'сокет\n', 'декоратор']

with open('test_file.txt', 'w') as f:
    f.writelines(words)
    print(f'Кодировка по умолчанию {f.encoding=}')

with open('test_file.txt', 'rb') as f:
    text_bytes = f.read()

info_about_text = chardet.detect(text_bytes)
default_codec = info_about_text['encoding']
text = text_bytes.decode(default_codec)


with open('test_file.txt', 'w', encoding='utf-8') as f:
    text = text.replace('\r', '')
    f.write(text)
