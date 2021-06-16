"""
Каждое из слов «class», «function», «method»
записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

bwords = [b'class', b'function', b'method']
print(*(f'"{word.decode("utf-8")}" - тип {type(word)}, длина: {len(word)}\n'
        for word in bwords), sep='')
