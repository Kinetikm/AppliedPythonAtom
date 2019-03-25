#!/usr/bin/env python
# coding: utf-8

import multiprocessing
import os


def check_encoding(path):
    encodings = ['utf-16', 'utf-8', 'cp1251']
    for i in encodings:
        try:
            open(path, encoding=i).read()
        except (UnicodeDecodeError, LookupError, UnicodeError):
            pass
        else:
            return i


def word_count_in_file(file_name, words_counter, path_to_dir, f_name):
    words = 0
    for line in file_name:
        words_in_line = line.split(' ')
        for i in words_in_line:
            if i == '\n':
                words_in_line.remove(i)
        words += len(words_in_line)
    path_str = path_to_dir + '/'
    words_counter[f_name.replace(path_str, '')] = words
    # total_words += words


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
    manager = multiprocessing.Manager()
    words_counter = manager.dict()
    # words_counter = dict()

    # открыл папку
    files_in_dir_temp = os.listdir(path_to_dir)

    # манипуляции
    path_str = path_to_dir + '/'
    files_in_dir = [path_str + i for i in files_in_dir_temp]

    try:
        dc_store = path_to_dir + '/' + '.DS_Store'
        files_in_dir.remove(dc_store)
    except (FileNotFoundError, ValueError):
        pass

    tasks = []
    for f_name in files_in_dir:
        enc = check_encoding(f_name)

        with open(f_name, encoding=enc) as file_name:

            task = multiprocessing.Process(target=word_count_in_file,
                                           args=(file_name, words_counter, path_to_dir, f_name,))
            tasks.append(task)
            task.start()
        file_name.close()

    for task in tasks:
        task.join()

    total_words = 0
    for item in words_counter.values():
        total_words += item

    words_counter['total'] = total_words

    return words_counter
