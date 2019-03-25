#!/usr/bin/env python
# coding: utf-8


from multiprocessing import Process, Manager
import os


def function(path_to_dir, name_of_file, result):
    file = open(path_to_dir + os.sep + name_of_file, encoding='utf8')
    num_of_words = 0
    char = file.read(1)
    while True:
        if char == '':
            break
        h = 0
        if char != ' ' and char != '\t' and char != '\n':
            h += 1
        char = file.read(1)
        if char == ' ' or char == '\t' or char == '\n' or char == '':
            h += 1
        if h == 2:
            num_of_words += 1
    file.close()
    result[name_of_file] = num_of_words


def word_count_inference(path_to_dir):
    list_of_files = os.listdir(path=path_to_dir)
    manager = Manager()
    result = manager.dict()
    tasks = []
    len_max = 4  # максимальное количество запущенных процессов одновременно
    for name_of_file in list_of_files:
        tasks.append(Process(target=function,
                    args=(path_to_dir, name_of_file, result)))
        tasks[-1].start() 
        i = 0
        while len(tasks) == len_max:
            if not tasks[i].is_alive():
                tasks.pop(i)
            elif i == len_max-1:
                i = 0
            else:
                i += 1
    for task in tasks:
        task.join()
    tasks.clear()
    total = 0
    for i in result.keys():
        total += result[i]
    result['total'] = total
    return result
