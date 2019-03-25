import multiprocessing
from multiprocessing import Process, Queue
import os
from time import time
import threading


class Word_counter:
    def __init__(self, path_to_dir):
        self.path_to_dir = path_to_dir
        self.last_file = ""
        self.num_words = dict()
        self.total = 0
        self._get_file_list()

    def _get_file_list(self):
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

    def _form_path_files(self, filename):
        path = self.path_to_dir.replace("\\", "/")
        path = path.strip("/")
        fullname = path + "/" + filename
        return fullname

    def _get_count_words(self, fullname, codec):
        num_words1 = 0
        with open(fullname, 'r', encoding=codec) as fd:
            for line in fd:
                if len(line) == 0:
                    num_words1 = 0
                    return num_words1
                else:
                    line_file = line.replace("\n", "")
                    line_file = line_file.replace("\r", "")
                    if (len(line_file) == 0):
                        num_words1 += 0
                    else:
                        line_file = line.split(" ")
                        num_words1 += len(line_file)
        return num_words1

    def creator(self, q):
        if len(self.files) > 0:
            for filename in self.files:
                q.put(filename)

    def counter_words(self, q, q1, d_dict):
        a = False
        while True:
            filename = q.get()
            fullname = self._form_path_files(filename)
            # codec = self._get_encoding(fullname)
            codec = "utf-8"
            num_words1 = self._get_count_words(fullname, codec)

            d_dict[filename] = num_words1
            q1.put(d_dict)
            self.num_words[filename] = num_words1

            if filename == self.last_file:
                break


def word_count_inference(path_to_dir):
    word_counter = Word_counter(path_to_dir)
    d_dict1 = dict()
    d_dict2 = dict()
    d_dict3 = dict()
    d_dict2["init"] = 0
    q = Queue()
    q1 = Queue()

    q1.put(d_dict2)

    process_one = Process(target=word_counter.creator, args=(q,))
    process_two = Process(target=word_counter.counter_words, args=(q, q1, d_dict1))
    process_one.start()
    process_two.start()
    process_one.join()
    process_two.join()

    for i in word_counter.files:
        d_dict3 = q1.get()
    d_dict3 = q1.get()

    total = 0
    for key, value in d_dict3.items():
        total += value
    d_dict3["total"] = total

    # print("dict: {}".format(d_dict3))

    q.close()
    q.join_thread()
    q1.close()
    q1.join_thread()
    return d_dict3

# dirname = "C:/Danila/python/AppliedPythonAtom/homeworks/homework_04/test_data"
# d_dict = word_count_inference(dirname)
# print("{}".format(d_dict))
