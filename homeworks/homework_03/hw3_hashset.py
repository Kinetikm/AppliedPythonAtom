#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):

        super().__init__()

    def get(self, key, default_value=None):

        return super().__contains__(key)

    def put(self, key, value):

        def put(self, key, value=None):

            return super().put(key, value)

    def __len__(self):

        return super().__len__()

    def values(self):

        return super().keys()

    def intersect(self, another_hashset):
        r
        New_set = HashSet()
        values = self.values() + another_hashset.values()
        for i in values:
            if i in self.values() and i in another_hashset.values():
                New_set.put(i)
        return New_set