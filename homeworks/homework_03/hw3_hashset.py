#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):
    plug = 'value'

    def __init__(self, bucket_num=64):
        # TODO Сделать правильно =)
        super().__init__(bucket_num)

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        return super().__contains__(key)

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, self.plug)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        result_hashset = HashSet(10)
        for value in self.values():
            if another_hashset.get(value):
                result_hashset.put(value)
        return result_hashset
