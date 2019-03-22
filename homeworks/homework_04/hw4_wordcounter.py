#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


def count_words(dirpath, filename, d):
    with open(dirpath + '/' + filename, 'r', encoding='utf8') as f:
        d[filename] = 0
        for line in f.readlines():
            d[filename] += len([w for w in line.split(" ") if w != '\n'])


def word_count_inference(path_to_dir):
    """
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    """

    try:
        manager = Manager()
        cnt = manager.dict()

        for f in os.listdir(path_to_dir):
            p = Process(target=count_words, args=(path_to_dir, f, cnt))
            p.start()
            p.join()

        cnt['total'] = sum(cnt.values())
        return cnt

    except UnicodeError:
        return {}
