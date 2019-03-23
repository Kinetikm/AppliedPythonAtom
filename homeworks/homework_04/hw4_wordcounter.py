#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool, Queue
import os


def count_of_words_in_file(full_path: str) -> int:
    """Возвращает количество слов в файле"""
    words_count = 0

    with open(full_path, mode='r') as f:
        for line in f:
            words_count += len(line.split())

    return words_count


def dir_files_to_queue(path_to_dir: str) -> Queue:
    """
    Помешает список путей до файлов из переданной директории в очередь
    Возвращает заполненную очередь (имя файла, путь)
    """
    queue = Queue()

    for f in os.listdir(path_to_dir):
        full_path = path_to_dir + '/' + f
        if os.path.isfile(full_path):
            queue.put([f, full_path])

    return queue


def word_count_inference(path_to_dir: str) -> dict:
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
    queue = dir_files_to_queue(path_to_dir)
    words = {'total': 0}

    with Pool(4) as p:
        while not queue.empty():
            file = queue.get()
            words_count = p.apply(count_of_words_in_file, (file[1], ))
            words[file[0]] = words_count
            words['total'] += words_count

    return words
