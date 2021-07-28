"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet


def ping(site):
    args = ['ping', site]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


ping('yandex.ru')
ping('youtube.com')


# с использованием chardet


def ping_chardet(site):
    args = ['ping', site]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        info_about_line = (chardet.detect(line))
        line = line.decode(info_about_line['encoding']).encode('utf-8')
        line = line.decode('utf-8')
        print(line)


ping_chardet('yandex.ru')
ping_chardet('youtube.com')
