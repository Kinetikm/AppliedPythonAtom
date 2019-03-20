#!/usr/bin/env python
# coding: utf-8


class HashMap:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            raise NotImplementedError
            return self.key

        def get_value(self):
            raise NotImplementedError
            return self.value

        def __eq__(self, other):
            raise NotImplementedError
            return self.key == other.key

    def __init__(self, bucket_num=64):

        raise NotImplementedError
        self.size = bucket_num
        self.hash_bucket = [None] * self.size

    def get(self, key, default_value=None):
        raise NotImplementedError
        x = self._get_hash(key)
        y = self._get_index(x)
        if self.hash_bucket[y] is not None:
            for i in self.hash_bucket(y):
                if i.get_key() == key:
                    return i.get_value()
        return default_value

    def put(self, key, value):
        raise NotImplementedError
        x = self._get_hash(key)
        y = self._get_index(x)
        if self.hash_bucket[y] is None:
            self.hash_bucket[y] = [self.Entry(key, value)]
        elif self.Entry(key, value) in self.hash_bucket[y]:
            for new_value in self.hash_bucket[y]:
                if new_value.key == key:
                    new_value.value = value
        else:
            self.hash_bucket[y].append(self.Entry(key, value))

    def __len__(self):
        raise NotImplementedError
        k = 0
        for i in self.hash_bucket:
            if i is not None:
                k += len(i)
        return k

    def _get_hash(self, key):
        raise NotImplementedError
    return hash(key)

    def _get_index(self, hash_value):
        raise NotImplementedError
        return hash_value % self.size

    def values(self):
        raise NotImplementedError
        return list(j.value for i in self.hash_bucket if i is not None for j in i)

    def keys(self):
        raise NotImplementedError
        return list(j.key for i in self.hash_bucket if i is not None for j in i)

    def items(self):
        raise NotImplementedError
        return list((j.key, j.value) for i in self.hash_bucket if i is not None
                    for j in i)

    def _resize(self):
        raise NotImplementedError
        self.hash_bucket += [None] * (self.size // 2)

    def __str__(self):
        raise NotImplementedError
        return "buckets: {}, items: {}".format(self.hash_bucket, self.items())

    def __contains__(self, item):
        raise NotImplementedError
        return item in self.keys()
