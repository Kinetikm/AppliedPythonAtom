#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap

# from hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        # raise NotImplementedError
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        # raise NotImplementedError
        return super().__contains__(key)

    def put(self, value):
        # TODO метод put, нужно переопределить данный метод
        # raise NotImplementedError
        return super().put(value, value)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        # raise NotImplementedError
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        # raise NotImplementedError
        return super().values()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        # raise NotImplementedError
        ret = HashSet()
        val = self.values()
        val2 = another_hashset.values()
        # val.extend(val2)
        for i in val:
            if i in val2:
                ret.put(i)
        return ret
