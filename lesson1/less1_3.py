"""
Определить, какие из слов
«attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""

word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

all_words = [word_1, word_2, word_3, word_4]

for word in all_words:
    try:
        print(bytes(word, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')
