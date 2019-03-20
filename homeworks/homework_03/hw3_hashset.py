#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        if key in self:
            return True
        else:
            return False

    def put(self, key, value=None):
        super().put(key, key)

    def __len__(self):
        return super().__len__()

    def values(self):
        return super().values()

    def intersect(self, another_hashset):
        return_hash_set = HashSet()
        for element in another_hashset.values():
            if element in self:
                return_hash_set.put(element)
        return return_hash_set
