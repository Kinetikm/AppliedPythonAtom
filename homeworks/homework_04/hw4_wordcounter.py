#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


def wordcount(que, fin):
    while que.qsize() > 0:
        path_to_dir, filename = que.get()
        path = path_to_dir + '/' + filename
        local = 0
        with open(path, encoding='utf-8') as f:
            for line in f:
                local += len(line.split())
        fin[filename] = local
        que.task_done()
        f.close()


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    # raise NotImplementedError
    fin = Manager().dict()
    que = Manager().Queue()
    file_list = os.listdir(path_to_dir)
    for i in file_list:
        que.put((path_to_dir, i))
    task = Process(target=wordcount, args=(que, fin,))
    task.start()
    task.join()
    fin['total'] = sum(fin.values())
    return fin
