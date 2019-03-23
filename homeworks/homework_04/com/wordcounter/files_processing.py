#!/usr/bin/env python
# coding: utf-8

import csv
import multiprocessing


def parseFilesSP(files, queue):
    for file in files:
        wordscount = 0
        with open(file=file, mode="r") as f:
            reader = csv.reader(f, delimiter=' ')
            for row in reader:
                wordscount += len(row)
        data = queue.get()
        filename = file[file.rfind('/') + 1:]
        data[filename] = wordscount
        data["total"] += wordscount
        queue.put(data)


def parseFiles(files) -> dict:
    num_processes = min(len(files), multiprocessing.cpu_count())
    tasks = []
    result = {"total": 0}
    q = multiprocessing.Queue()
    q.put(result)
    for cur_process in range(num_processes):
        files_for_process = []
        for index in range(cur_process, len(files), num_processes):
            files_for_process.append(files[index])
        task = multiprocessing.Process(target=parseFilesSP, args=(files_for_process, q))
        tasks.append(task)
        task.start()
    for task in tasks:
        task.join()
    result = q.get()
    return result
