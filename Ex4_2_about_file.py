# Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах).
import io
import os
# создание итерируемого объекта = строки файла
main_iter = io.open('FIRST_FILE')

x = 0
f2 = open('SECOND_FILE', 'w')     # clear file
# проход по итерируемому объекту с помощью цикла
for st in main_iter:
    even_st = st
    x += 1                        # вывод номера строки
    if x % 2 == 0:
        print("строка №", x, "   ", even_st)
        f2.write(even_st)

f2.close()

with open("FIRST_FILE") as file:

    file.seek(0, os.SEEK_END)
    print("размер файла F1", file.tell(), "в байтах ")

with open("SECOND_FILE") as file:

    file.seek(0, os.SEEK_END)
    print("размер файла F2", file.tell(), "в байтах ")
