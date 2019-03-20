#!/usr/bin/env python
# coding: utf-8
import time


class Bucket:
    def __init__(self, result, *args, **kwargs):
        self.value = (args, kwargs)
        self.result = result


class LRUCacheDecorator:
    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        # raise NotImplementedError
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = []
        self.time = time.time()

    def put(self, val):
        if len(self.cache) == self.maxsize:
            self.cache.pop()
            self.cache.insert(0, val)
        else:
            self.cache.insert(0, val)

    def __call__(self, func):
        # TODO вызов функции
        # raise NotImplementedError
        def _dec(*args, **kwargs):
            if self.ttl is not None and time.time() - self.time > self.ttl:
                self.cache = []
            value = (args, kwargs)
            for i in self.cache:
                if i.value == value:
                    self.cache.remove(i)
                    self.cache.insert(0, i)
                    return i.result
            res = func(*args, **kwargs)
            val = Bucket(res, *args, **kwargs)
            self.put(val)
            self.time = time.time()
            return res
        return _dec
