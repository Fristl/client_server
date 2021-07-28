"""
1. Каждое из слов «разработка», «сокет», «декоратор»
представить в строковом формате и проверить тип и
содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""

word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
words = [word_1, word_2, word_3]
print(*(f'"{word}" тип {type(word)}\n' for word in words), sep='')

uni_word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
uni_word_2 = '\u0441\u043e\u043a\u0435\u0442'
uni_word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
uni_words = [uni_word_1, uni_word_2, uni_word_3]

print(*(f'"{uni_word}" тип {type(uni_word)}\n' for uni_word in uni_words), sep='')
print('*' * 30)

for word in words:
    print(f'"{word}" тип {type(word)}')
    print(f'"{word.encode("unicode_escape").decode("utf-8")}" тип {type(word)} в формате кодовых точек')
