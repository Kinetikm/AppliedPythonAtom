#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


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
    d = Manager().dict()
    tasks = []
    files = list(i for i in os.listdir(path_to_dir))
    for f in files:
        p = Process(target=cnt, args=(path_to_dir + '/' + f, d))
        tasks.append(p)
        p.start()
    for task in tasks:
        task.join()
    d['total'] = sum(d.values())
    return d


def cnt(filename, d):
    number = 0
    with open(filename, encoding='utf-8') as f:
        for word in f:
            number += len(word.split())
    d[filename.split('/')[-1]] = number
