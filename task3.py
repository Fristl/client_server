"""
Определить, какие из слов
«attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""

word1 = b'attribute'
word2 = b'класс'  # SyntaxError: bytes can only contain ASCII literal characters.
word3 = b'функция'
word4 = b'type'

# в байтовом типе работает кодировка ASCII,
# которая не поддерживает кириллицу
