#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    # не увидел смысла переопределять __init__
    # (разве что ради переобозначения атрибута map)
    
    def get(self, value):
        if self.map[hash(value) % self.max_size].count(value):
            return True
        return False

    def put(self, value):
        if not self.map[hash(value) % self.max_size].count(value):
            self.map[hash(value) % self.max_size].append(value)
        
        # встает вопрос о необходимости расширения hashset
        # в случае ее присутствия необходимо переопределить метод _resize

    # метод __len__ будет работать исправно

    def values(self):
        result = []
        for i in self.map:
            result.extend(i)
        return result

    def intersect(self, another_hashset):
        i = 0
        # создаем новый hashset оптимального размера
        res_hashset = HashSet(min(another_hashset.max_size, self.max_size))
        h = set(self.values())
        h.intersection_update(set(another_hashset.values()))
        h = list(h)
        for i in h:
            res_hashset.put(i)
        return res_hashset
        
    def __contains__(self, item):
        for i in self.map:
            if i.count(item):
                return True
        return False
