#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool
from functools import partial
from os import listdir


results_dict = {}


def read_file(filename, path_to_dir, results_dict):
    with open(path_to_dir + '/' + filename, "r") as file:
        results_dict[filename] = len(file.read().split())


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
    pool = Pool(8)
    allfiles = listdir(path_to_dir)
    pool.map(partial(read_file, path_to_dir, results_dict), allfiles)
    pool.close()
    pool.join()
    results_dict['total'] = sum(results_dict.values())
    return results_dict
