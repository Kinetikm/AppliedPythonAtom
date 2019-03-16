#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        return super().__contains__(key)

    def put(self, key, value=None):
        super().put(key, None)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().keys()

    def intersect(self, another_hashset):
        res = HashSet()
        for item in another_hashset.items():
            if item[0] in self.keys():
                res.put(item[0], None)
        return res
