#!/usr/bin/env python
# coding: utf-8

from collections import *
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = {}
        self.lru = []
        self.time = time.time()

    def put(self, func, res):
        if len(self.lru) == self.maxsize:
            self.cache.pop(self.lru[-1])
            self.lru.pop()
            self.lru.insert(0, func)
            self.cache[func] = res
        else:
            self.cache[func] = res
            self.lru.insert(0, func)

    def __call__(self, func):
        # TODO вызов функции
        def _dec(*args, **kwargs):
            if self.ttl is not None and time.time() - self.time > self.ttl:
                self.cache = {}
                self.lru = []
            value = str(args) + str(kwargs)
            if self.cache.get(value) is not None:
                self.lru.remove(value)
                self.lru.insert(0, value)
                return self.cache[value]
            res = func(*args, **kwargs)
            self.put(value, res)
            self.time = time.time()
            return res

        return _dec
