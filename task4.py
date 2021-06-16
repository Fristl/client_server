"""
Преобразовать слова
«разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for enc_word in words:
    benc = enc_word.encode("utf-8")
    denc = benc.decode("utf-8")
    print(f'Cлово "{enc_word}" в байтовом виде: {benc} {type(benc)} '
          f'\nи снова в виде строки "{denc}" {type(denc)}\n')
