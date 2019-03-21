#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return True if super().get(key, default_value) is not None else False

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, key)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        res_hashset = HashSet()
        for item in another_hashset.items():
            if (item[0] in self):
                res_hashset.put(item[0], item[0])
        return res_hashset
