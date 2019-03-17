#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):
    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    # def get(self, key, default_value=None):
    # TODO достаточно переопределить данный метод

    def put(self, key):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, 1)

    # def __len__(self):
    # TODO Возвращает количество Entry в массиве

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        out = HashSet()
        for a in self.values():
            if another_hashset.get(a) is not None:
                out.put(a)
        return out
