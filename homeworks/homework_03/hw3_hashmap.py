#!/usr/bin/env python
# coding: utf-8


class HashMap:
    fill_factor =  1/3
    exp_coeff = 2
    class Entry:
        def __init__(self, key, value):
            self.inf = (key, value)

        def get_key(self):
            return self.inf[0]

        def get_value(self):
            return self.inf[1]

        def __eq__(self, other):
            if self.get_key() == other.get_key():
                return True
            return False

    def __init__(self, bucket_num=64):
        self.max_size = bucket_num
        self.present_size = 0
        i = 0
        self.map = []
        while i < self.max_size:
            self.map.append([])
            i += 1

    def get(self, key, default_value=None):
        h = hash(key)%self.max_size
        i = 0
        while i < len(self.map[h]):
            if self.map[h][i].get_key() == key:
                return self.map[h][i].get_value()
            i += 1
        return default_value

    def put(self, key, value):
        h = hash(key)%self.max_size
        element = self.Entry(key, value)
        if not self.map[h]:
            self.map[h].append(element)
            self.present_size += 1
            if self.present_size >= self.max_size*self.fill_factor:
                self._resize()
        else:
            i = 0
            while i < len(self.map[h]):
                if self.map[h][i].__eq__(element):
                    self.map[h].pop(i)
                    break
                i += 1
            self.map[h].append(element)

    def __len__(self):
        i = 0
        result = 0
        while i < self.max_size:
            result += len(self.map[i])
            i += 1
        return result

    def _get_hash(self, key):
        return hash(key)

    def _get_index(self, hash_value):
        return hash_value % self.max_size

    def values(self):
        result = []
        for i in self.map:
            for j in i:
                result.append(j.get_value())
        return result

    def keys(self):
        result = []
        for i in self.map:
            for j in i:
                result.append(j.get_key())
        return result

    def items(self):
        result = []
        for i in self.map:
            for j in i:
                result.append(j.inf)
        return result

    def _resize(self):
        self.max_size *= self.exp_coeff
        self.present_size = 0
        help_list = self.items()
        self.map = []
        i = 0
        while i < self.max_size:
            self.map.append([])
            i += 1
        for i in help_list:
            self.put(i[0], i[1])
        help_list = self.items()

    def __str__(self):
        # метод выводит лишь непустые 'buckets' и их 'items'
        i = 0
        help_list1 = []
        help_list2 = []
        while i < self.max_size:
            if self.map[i]:
                help_list1.append(i)
                help_list2.append([])
                for j in self.map[i]:
                    help_list2[-1].append(j.inf)
            i += 1
        return 'buckets: {}, items: {}'.format(help_list1, help_list2)

    def __contains__(self, item):
        for i in self.map:
            for j in i:
                if j.get_key() == item or j.get_value() == item:
                    return True
        return False
