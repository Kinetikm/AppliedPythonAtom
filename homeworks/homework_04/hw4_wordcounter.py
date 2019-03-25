#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


def count_words_in_file(queue, main_dict):
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
    main_dict = Manager().dict()
    queue = Manager().Queue()
    procs = []
    file_names = list(os.listdir(path_to_dir))
    for name in file_names:
        queue.put((path_to_dir, name))
    for _ in range(4):
        p = Process(target=count_words_in_file, args=(queue, main_dict))
        procs.append(p)
        p.start()
    for p in procs:
        if p.is_alive():
            p.join()

    main_dict['total'] = sum(main_dict.values())
    return main_dict
