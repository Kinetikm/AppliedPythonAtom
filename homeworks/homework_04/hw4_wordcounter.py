#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Manager, Process, Lock
import os

queue = Manager().Queue()
dict_return = Manager().dict()


def dict_count():
    while queue.qsize() > 0:
        try:
            path_to_dir, filename = queue.get()
            with open(path_to_dir + '/' + filename, "r",
                      encoding='utf8') as file:
                dict_return[filename] = len(file.read().split())
            queue.task_done()
        except EOFError:
            return


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
    processes = []
    for file in os.listdir(path_to_dir):
        queue.put((path_to_dir, file))
    for i in range(4):
        process = Process(target=dict_count)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    dict_return['total'] = sum(dict_return.values())
    return dict_return
