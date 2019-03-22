#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import glob
import os
from os import listdir
from os.path import isfile, join


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

    onlyfiles = list()
    for file in os.listdir(path_to_dir):
        onlyfiles.append(file)

    def countword(filename, path, d):

        n = 0
        with open(str(path) + "/" + str(filename)) as f:
            for line in f:
                l = line.split(" ")
                for w in l:
                    if w != "" and w != " " and w != "\n":
                        n += 1
        d[filename] = n
        d["total"] += n

    with Manager() as manager:
        d = manager.dict()
        d["total"] = 0
        for files in onlyfiles:
            p = Process(target=countword, args=(files, path_to_dir, d))
            p.start()
            p.join()
        s = d.copy()
    return s
