#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Manager, Pool
import os


def _word_count_task(path_to_dir, filename, counter):
    res = 0
    with open(os.path.join(path_to_dir, filename), 'r') as f:
        for line in f:
            res += len(line.split())
    # Не большая проблема с шаред памятью.. но ладно
    counter[filename] = res


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
    counter = manager.dict()

    with Pool(os.cpu_count()) as p:
        p.starmap(_word_count_task, [(path_to_dir, filename, counter) for filename in os.listdir(path_to_dir)])
    return {'total': sum(counter.values()), **counter}
