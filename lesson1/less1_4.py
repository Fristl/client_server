"""
Преобразовать слова
«разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'
all_words = [word_1, word_2, word_3, word_4]

for word in all_words:
    word_in_bytes = word.encode("utf-8")
    decode_word_in_bytes = word_in_bytes.decode("utf-8")
    print(f'Слово "{word}" в байтовом виде: {word_in_bytes} {type(word_in_bytes)} '
          f'\nи снова в виде строки "{decode_word_in_bytes}" {type(decode_word_in_bytes)}\n')
