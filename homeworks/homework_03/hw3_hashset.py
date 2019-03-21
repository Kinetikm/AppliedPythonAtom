#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self, bucket_num=64):
        # TODO Сделать правильно =)
        super().__init__(bucket_num)

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        result = super().get(key)
        if result is not None:
            return True
        else:
            return default_value

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, key)

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
        for element in another_hashset.values():
            if element in self.values():
                result.put(element, None)
        return result
