#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:09:57 2019

@author: dmitry
"""

from multiprocessing import Queue, Process
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