import chardet
import subprocess
import platform
import locale

print('====== Задание 1 ======')


def my_print(string, variable_name, variable_len=0):
    print(f'Переменная {variable_name}: "{string}" типа {type(string)}')
    if variable_len:
        print(f'длина переменной {variable_name}: {variable_len}')


exem1_str_1 = 'разработка'
exem1_str_2 = 'сокет'
exem1_str_3 = 'декоратор'
my_print(exem1_str_1, 'exem1_str_1')
my_print(exem1_str_2, 'exem1_str_2')
my_print(exem1_str_3, 'exem1_str_3')
print("======")
exem1_str_1_uni = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
exem1_str_2_uni = '\u0441\u043e\u043a\u0435\u0442'
exem1_str_3_uni = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
my_print(exem1_str_1_uni, 'exem1_str_1_uni')
my_print(exem1_str_2_uni, 'exem1_str_2_uni')
my_print(exem1_str_3_uni, 'exem1_str_3_uni')

print('====== Задание 2 ======')


def str_to_byte(string):
    try:
        byts = eval(f'b"{string}"')
    except SyntaxError:
        return False
    return byts


exem2_byte_1 = str_to_byte('class')
exem2_byte_2 = str_to_byte('function')
exem2_byte_3 = str_to_byte('method')
my_print(exem2_byte_1, 'exem2_byte_1', len(exem2_byte_1))
my_print(exem2_byte_2, 'exem2_byte_2', len(exem2_byte_2))
my_print(exem2_byte_3, 'exem2_byte_3', len(exem2_byte_3))

print('====== Задание 3 ======')
exem3_words = ['attribute', 'класс', 'функция', 'type']
for exem3_word in exem3_words:
    exem3_byte = str_to_byte(exem3_word)
    if exem3_byte:
        print(f'"{exem3_word}" возможно записать в байтовом типе ')
    else:
        print(f'"{exem3_word}" невозможно записать в байтовом типе')

print('====== Задание 4 ======')
exem4_words = ['разработка', 'администрирование', 'protocol', 'standard']
for exem4_word in exem4_words:
    exem4_byte = exem4_word.encode('utf-8')
    exem4_word_decoded = exem4_byte.decode('utf-8')
    my_print(exem4_byte, f'[{exem4_word}]')
    print(f'результат декодирования в utf-8: {exem4_word_decoded} для {exem4_word}')

print('====== Задание 5 ======')

default_encoding = locale.getpreferredencoding()
param = '-n' if platform.system().lower() == 'windows' else '-c'
sites_to_ping = ['yandex.ru', 'youtube.com']
for site_to_ping in sites_to_ping:
    print(f'=== Результаты PING-а сайта {site_to_ping} ===')
    args = ['ping', param, '2', site_to_ping]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        line = line.decode(default_encoding).encode('utf-8')
        print(line.decode('utf-8'))

print('====== Задание 6 ======')
with open("test_file.txt", 'rb') as file:
    content = file.read()
encoding = chardet.detect(content)['encoding']
print(f'Кодировка по умолчанию: {encoding}')
with open("test_file.txt", 'r', encoding=encoding) as file_read:
    for exem6_str in file_read:
        print(exem6_str, end='')

