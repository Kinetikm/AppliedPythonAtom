#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_04.com.wordcounter import files_processing
from homeworks.homework_04.com.wordcounter import path_processing


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
    files = path_processing.getFiles(path_to_dir)
    if files:
        return files_processing.parseFiles(files)
    else:
        return {"total": 0}
