#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super(HashSet, self).__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        if key in self:
            return True
        else:
            return False

    def put(self, key, value=None):
        super().put(key, None)

    def values(self):
        return self.keys()

    def intersect(self, another_hashset):
        res = HashSet()
        for key in self.values():
            if another_hashset.get(key):
                res.put(key)
        return res
