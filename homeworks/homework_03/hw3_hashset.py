#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap
# from hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return super().__contains__(key)
        # return super().get(key)

    def put(self, value):
        # TODO метод put, нужно переопределить данный метод
        return super().put(value, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        result = HashSet()
        values1 = self.values()
        values2 = another_hashset.values()
        values3 = values1 + values2
        for i in values3:
            if i in values1 and i in values2:
                result.put(i)

        return result
