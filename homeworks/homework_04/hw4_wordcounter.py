#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Queue
from os import listdir
from os.path import isfile, join


def word_count_inference(path_to_dir='./test_data'):
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
    files = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
    q = Queue()
    words_count = {}
    tasks = []
    words_count['total'] = 0
    for file in files:
        path = path_to_dir + "/" + file
        print(path)
        task = Process(target=count_words_in_file, args=(path, q, ))
        tasks.append(task)
        task.start()
        words_count[file] = q.get()
    for task in tasks:
        task.join()
    for x in words_count.keys():
        words_count['total'] += words_count[x]
    print(words_count)
    return words_count


def count_words_in_file(path, q):
    with open(path, 'r') as f:
        data = f.read()
        x = data.split()
    f.closed
    q.put(len(x))
