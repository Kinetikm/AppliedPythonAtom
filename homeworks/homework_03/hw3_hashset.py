#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # достаточно переопределить данный метод
        if super().get(key) is not None:
            return True
        else:
            return False

    def put(self, key):
        # метод put, нужно переопределить данный метод
        super().put(key, key)

    def __len__(self):
        # Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # метод, возвращающий новый HashSet
        # элементы - пересечение текущего и другого
        hs = HashSet()
        for entry in self.values():
            if entry in another_hashset:
                hs.put(entry)
        return hs
