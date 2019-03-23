#!/usr/bin/env python
# coding: utf-8

import os


def getFiles(path_to_dir) -> list:
    if not os.path.exists(path_to_dir):
        return []
    objects = os.listdir(path=path_to_dir)
    files = []
    for object in objects:
        path_to_object = "".join([path_to_dir, "/", object]) \
            if path_to_dir[len(path_to_dir) - 1] != "/" \
            else "".join([path_to_dir, object])
        if os.path.isfile(path_to_object):
            files.append(path_to_object)
    return files
