#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Process, Manager, Queue, Lock
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

    q = Queue()

    word_cnt = Manager().dict()
    word_cnt['total'] = 0

    for file in os.listdir(path_to_dir):
        q.put((path_to_dir, file))

    try:
        tasks = [Process(target=word_counter, args=(q, word_cnt)) for _ in range(2)]

        for task in tasks:
            task.start()

        for task in tasks:
            task.join()
    except FileExistsError:
        return

    return word_cnt


def word_counter(q, cnt):

    print(q, cnt)

    while q.qsize() > 0:
        path, file = q.get()
        counter = 0
        with open(os.path.join(path, file), 'r') as data_file:
            data = data_file.readlines()
            not_empty = list(filter(lambda x: x != "\n", data))
            for i in not_empty:
                counter += len(i.split(" "))
        cnt[file] = counter
        cnt['total'] += counter
