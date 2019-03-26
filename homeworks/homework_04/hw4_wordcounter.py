#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager, Pool
import functools
import os

dict = Manager().dict()


def read_file(namefile, pth):
    with open(pth + '/' + namefile) as f:
        dict[namefile] = len(f.read().split())


def word_count_inference(path_to_dir):
    pool = Pool()
    list_of_files = os.listdir(path_to_dir)
    pool.map(functools.partial(read_file, pth=path_to_dir), list_of_files)
    pool.close()
    pool.join()
    dict['total'] = sum(dict.values())
    return dict
