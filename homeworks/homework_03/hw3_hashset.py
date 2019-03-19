#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return super().__contains__(key)

    def put(self, key, value=None):
        # print()
        # TODO метод put, нужно переопределить данный метод
        super().put(key, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        NewHash = HashSet()
        for element in another_hashset.items():
            if element[0] in self.keys():
                NewHash.put(element)
        return NewHash
