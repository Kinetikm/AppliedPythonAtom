#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool, Queue, cpu_count
from collections import deque
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
    result_dict = {"total": 0}  # Результирующий словарь
    total_count = 0  # Суммарное число слов во всех файлах
    files_list = create_deque(path_to_dir)
    p = Pool(cpu_count())
    with p:
        while files_list:
            filename = files_list.pop()
            count = p.apply(words_counter, (path_to_dir + "/" + filename,)).get()
            total_count += count
            result_dict.update({filename: count})
    p.close()
    p.join()
    result_dict.update({"total": total_count})
    return result_dict


def words_counter(filename):
    num_words = 0
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    f.close()
    return num_words


def create_deque(path_to_dir):
    files = deque()
    files.append(os.listdir(path_to_dir))
    return files
