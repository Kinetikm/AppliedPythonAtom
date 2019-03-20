#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        # достаточно переопределить данный метод
        return key in list(self.values())

    def put(self, key, value=None):
        super().put(key, None)

    def values(self):
        # возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        intersect_set = HashSet()

        for it in another_hashset.values():
            if self.get(it):
                intersect_set.put(it)
        return intersect_set
