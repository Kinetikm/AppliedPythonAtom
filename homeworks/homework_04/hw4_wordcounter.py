#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os
import re


def word_count(path_to_dir, file, dict_of_files, queue):
    with open(path_to_dir + '/' + file, "r", encoding="UTF8") as fh:
        words = re.split(r'\s+', fh.read())
    if words[0] == '':
        dict_of_files[file] = 0
    else:
        dict_of_files[file] = len(words)
        value = queue.get()
        queue.put(value + len(words))


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
    manager = Manager()
    dict_of_files = manager.dict()
    queue = manager.Queue()
    queue.put(0)
    process_list = []
    files = os.listdir(path_to_dir)
    for file in files:
        proc = Process(target=word_count, args=(path_to_dir, file, dict_of_files, queue))
        proc.start()
        process_list.append(proc)
    for proc in process_list:
        proc.join()
    dict_of_files["total"] = queue.get()
    return dict_of_files
