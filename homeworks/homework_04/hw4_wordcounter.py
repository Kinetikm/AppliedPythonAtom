#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


def count_words(queue, main_dict):
    while not queue.empty():
        file_path, name = queue.get()
        try:
            with open(file_path + '/' + name, "r", encoding='utf8') as file:
                main_dict[name] = len(file.read().split())
            queue.task_done()
        except FileNotFoundError:
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
    out_dict = Manager().dict()
    queue = Manager().Queue()
    procs = []
    for name in list(os.listdir(path_to_dir)):
        queue.put((path_to_dir, name))
    for _ in range(4):
        p = Process(target=count_words, args=(queue, out_dict))
        procs.append(p)
        p.start()
    for p in procs:
        if p.is_alive():
            p.join()

    out_dict['total'] = sum(out_dict.values())
    return out_dict
