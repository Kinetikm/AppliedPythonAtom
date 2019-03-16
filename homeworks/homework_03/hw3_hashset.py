#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()
        raise NotImplementedError

    def get(self, key, default_value=None):
        return super().get(key, default_value)

    def put(self, key, value):
        super().put(key, value)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().values()

    def intersect(self, another_hashset):
        res = HashSet()
        for item in another_hashset.items():
            if item.get_key() in self.keys():
                res.put(item.get_key(), item.get_value())
        return res
