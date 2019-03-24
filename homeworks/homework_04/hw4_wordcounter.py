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
    list_of_files = list(os.listdir(path_to_dir))
    wordmap = Manager().dict()
    list_of_procs = []

    def count_words_in_file(file_path, file_name, wordmap):
        counter = 0
        with open(file_path + '/' + file_name, 'r') as fh:
            lines = fh.readlines()
            not_empty = list(filter(lambda x: x != "\n", lines))
            for i in not_empty:
                counter += len(i.split(" "))
        wordmap[file_name] = counter
        wordmap['total'] += counter

    wordmap['total'] = 0
    for file in list_of_files:
        process = Process(target=count_words_in_file, args=(path_to_dir, file, wordmap))
        list_of_procs.append(process)
        process.start()
    for pr in list_of_procs:
        pr.join()
    return wordmap
