#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        other = self.Entry(key, key)
        for i in self.__table[self._get_index(self._get_hash(key))]:
            if i == other:
                return True
        return False

    def put(self, value):
        # TODO метод put, нужно переопределить данный метод
        super().put(value, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        result_hashset = HashSet()
        for i in super().items():
            if i in another_hashset:
                result_hashset.put(i)
        return result_hashset
