#!/usr/bin/env python
# coding: utf-8


from multiprocessing import Process, Manager
import multiprocessing
from multiprocessing import Process, Queue
import os
from time import time
import threading
from chardet.universaldetector import UniversalDetector


class WordCounter:
    def __init__(self, path_to_dir):
        self.path_to_dir = path_to_dir
        self.last_file = ""
        self.num_words = dict()
        self.total = 0
        self._get_list_of_files()

    def _get_list_of_files(self):
        try:
            self.files = os.listdir(self.path_to_dir)
            if len(self.files) == 0:
                print("this directory is empty")
                self.num_words = None
            else:
                self.last_file = self.files[-1]
        except FileNotFoundError:
            print("this dir is not correct!")
            self.files = None

    def _get_codec(self, filename):
        detector = UniversalDetector()
        try:
            with open(filename, 'rb') as file:
                for line in file:
                    detector.feed(line)
                    if detector.done:
                        break
                if os.path.getsize(filename) == 0:
                    return "empty"
                detector.close()
                result = detector.result['encoding']
                return result
        except FileNotFoundError:
            return None

    def _edit_filepath(self, filename):
        path = self.path_to_dir.replace("\\", "/")
        path = path.strip("/")
        fullname = path + "/" + filename
        return fullname

    def _get_count_words(self, fullname, codec):
        count_words = 0
        with open(fullname, 'r', encoding=codec) as fd:
            for line in fd:
                if len(line) == 0:
                    count_words = 0
                    return count_words
                else:
                    line_file = line.replace("\n", "")
                    line_file = line_file.replace("\r", "")
                    if len(line_file) == 0:
                        count_words += 0
                    else:
                        line_file = line.split(" ")
                        count_words += len(line_file)
        return count_words

    def create_queue(self, queue1):
        if len(self.files) > 0:
            for filename in self.files:
                queue1.put(filename)

    def counter_words(self, queue1, queue2, d_dict):
        while True:
            filename = queue1.get()
            fullname = self._edit_filepath(filename)
            codec = self._get_codec(fullname)
            if codec is None:
                print("file not found")
            elif codec == "empty":
                count_words = 0
            else:
                count_words = self._get_count_words(fullname, codec)
            d_dict[filename] = count_words
            queue2.put(d_dict)
            if filename == self.last_file:
                break


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
    word_counter = WordCounter(path_to_dir)
    dict1 = dict()
    dict2 = dict()
    dict3 = dict()
    queue1 = Queue()
    queue2 = Queue()
    queue2.put(dict2)
    process_one = Process(target=word_counter.create_queue, args=(queue1,))
    process_two = Process(target=word_counter.counter_words, args=(queue1, queue2, dict1))
    process_one.start()
    process_two.start()
    process_one.join()
    process_two.join()
    for f in word_counter.files:
        queue2.get()
    dict3 = queue2.get()
    total = 0
    for k, v in dict3.items():
        total += v
    dict3["total"] = total
    queue1.close()
    queue1.join_thread()
    queue2.close()
    queue2.join_thread()
    return dict3
