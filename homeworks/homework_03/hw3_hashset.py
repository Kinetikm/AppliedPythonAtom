#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):
    DEF_LEN = 4

    def get(self, value, default_value=None):
        return True if super().get(value, default_value) is not None else False

    def put(self, key, value=None):
        super().put(key, key)

    def intersect(self, another_hashset):
        """
        Метод, возвращающий новый HashSet
        содержащий в себе пересекающиеся элементы
        пересечения текущего и другого HashSet's
        """
        new_hashset = HashSet()

        for item in self.values():
            if another_hashset.get(item, None):
                new_hashset.put(item)

        return new_hashset

    def union(self, another_hashset):
        """
        Метод, возвращающий новый HashSet
        содержащий в себе все элементы
        из текущего и другого HashSet's
        """
        new_hashset = HashSet()

        values = self.values() + another_hashset.values()

        for item in values:
            new_hashset.put(item)

        return new_hashset
