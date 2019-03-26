#!/usr/bin/env python
# coding: utf-8


from multiprocessing import Process, Manager, Queue, Pool
import os


def amount_of_files_words(file):
    amount_of_words = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            amount_of_words += len(line.split())
    return amount_of_words


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
    total_words = 0
    Dict = {}
    q = Queue()
    for file in os.listdir(path_to_dir):
        q.put(file)
    with Pool(4) as p:
        while q.empty() is False:
            file = q.get()
            path_to_file = path_to_dir + '/' + file
            amount_of_words = p.apply(amount_of_files_words, (path_to_file,))
            Dict[file] = amount_of_words
            total_words += amount_of_words
    Dict['total'] = total_words
    return Dict
