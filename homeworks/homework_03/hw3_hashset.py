#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self, bucket_num=64):
        # TODO Сделать правильно =)
        return super().__init__(bucket_num)

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        if key in self:
            return True
        else:
            return False

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        return super().put(key, key)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_set = HashSet()
        for element in self.values():
            if element in another_hashset.values():
                new_set.put(element)
        return new_set
