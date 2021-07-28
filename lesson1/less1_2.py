"""
Каждое из слов «class», «function», «method»
записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

in_bytes_words = [b'class', b'function', b'method']
print(*(f'{word} - тип {type(word)}, длина: {len(word)}\n'
        for word in in_bytes_words), sep='')
