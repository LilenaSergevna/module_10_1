# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time=time.time()
write_words(10,'example1.txt')
write_words(30,'example2.txt')
write_words(200,'example3.txt')
write_words(100,'example4.txt')
print(f'Работа потоков {time.time()-start_time}')
start_time=time.time()

potok1=threading.Thread(target=write_words, args=(10,'example5.txt'))
potok1.start()
potok2=threading.Thread(target=write_words, args=(30,'example6.txt'))
potok2.start()
potok3=threading.Thread(target=write_words, args=(200,'example7.txt'))
potok3.start()
potok4=threading.Thread(target=write_words, args=(100,'example8.txt'))
potok4.start()
potok1.join()
potok2.join()
potok3.join()
potok4.join()
print(f'Работа потоков {time.time()-start_time}')