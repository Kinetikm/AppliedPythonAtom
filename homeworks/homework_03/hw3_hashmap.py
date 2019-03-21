#!/usr/bin/env python
# coding: utf-8


class HashMap:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def __eq__(self, other):
            result = self.key == other.key
            return result

    def __init__(self, bucket_num=64):
        self.buckets = bucket_num * [None]

    def get(self, key, default_value=None):
        if self.buckets[self._get_index(self._get_hash(key))] is not None:
            for i in self.buckets[self._get_index(self._get_hash(key))]:
                if i.get_key() == key:
                    return i.get_value()
        return default_value

    def put(self, key, value):
        if self.buckets[self._get_index(self._get_hash(key))] is None:
            self.buckets[self._get_index(self._get_hash(key))] = [self.Entry(key, value)]
        elif self.Entry(key, value) in self.buckets[self._get_index(self._get_hash(key))]:
            for i in self.buckets[self._get_index(self._get_hash(key))]:
                if i.key == key:
                    i.value = value
        else:
            self.buckets[self._get_index(self._get_hash(key))].append(self.Entry(key, value))

    def __len__(self):
        long = 0
        for i in self.buckets:
            if i is not None:
                long += len(i)
        return long

    def _get_hash(self, key):
        return hash(key)

    def _get_index(self, hash_value):
        return hash_value % len(self.buckets)

    def values(self):
        return [j.value for i in self.buckets
                if i is not None
                for j in i]

    def keys(self):
        return [j.key for i in self.buckets if i is not None
                for j in i]

    def items(self):
        return [(j.key, j.value) for i in self.buckets
                if i is not None for j in i]

    def _resize(self):
        self.buckets += (len(self.buckets) // 2) * [None]

    def __str__(self):
        return "buckets: {}, items: {}".format(self.buckets, self.items())

    def __contains__(self, item):
        return item in self.keys()
