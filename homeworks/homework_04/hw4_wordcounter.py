#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Queue
import os


def get_files(path_to_dir, q1):
    for file in os.listdir(path_to_dir):
        q1.put(file)


def get_info(q, filename):
    with open('test_data/' + filename, 'r', encoding='UTF8') as f:
        q.put(f.readlines())


def counter(info):
    word_counter = 0
    for line in info:
        word_counter += len(line.split())
    return word_counter


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
    q1 = Queue()
    word_counter = 0
    words = {'total': 0}
    p = Process(target=get_files, args=(path_to_dir, q1,))
    p.start()
    p.join()
    while not q1.empty():
        file = q1.get()
        task = Process(target=get_info, args=(q, file))
        task.start()
        word_counter = counter(q.get())
        words[file] = word_counter
        words['total'] += word_counter
    return words
