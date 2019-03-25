#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager, Pool
from subprocess import Popen, PIPE, STDOUT
import os


def counter(filename):
    cmd = f"cat {filename} | wc -w"
    ps = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = int(ps.communicate()[0].strip())
    return os.path.split(filename)[-1], output


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
    p = Pool(10)
    fullpaths = map(lambda x: f'{path_to_dir}/{x}', os.listdir(path_to_dir))
    out = p.map(counter, fullpaths)
    counts_words = {}
    for filename, c in out:
        counts_words[filename] = c
    counts_words["total"] = sum(counts_words.values())
    return counts_words
