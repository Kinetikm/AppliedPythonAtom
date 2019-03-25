#!/usr/bin/env python
# coding: utf-8


from multiprocessing import Process, Manager
from os import listdir


def ProcFunction(path_to_file, filename, OutDict):
    counter = 0
    with open(path_to_file + '/' + filename, "r",
              encoding='utf8') as fd:
        for line in fd:
            counter += len(line.split())
        fd.close()
    OutDict[filename] = counter
    OutDict["total"] += counter


def word_count_inference(path_to_dir):
    OutDict = Manager().dict({"total": 0})
    bufferForProc = list()
    for filename in listdir(path_to_dir):
        procces_1 = Process(target=ProcFunction(path_to_dir,
                                                filename, OutDict))
        bufferForProc.append(procces_1)
        procces_1.start()

    for proc in bufferForProc:
        proc.join()
    return OutDict
