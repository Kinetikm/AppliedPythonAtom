#!/usr/bin/env python
# coding: utf-8
from collections import deque
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = deque()
        self.timestart = time.time()

    def put(self, function, result):
        if len(self.cache) < self.maxsize:
            self.cache.appendleft({'args': function, 'result': result})
        else:
            self.cache.pop()
            self.cache.appendleft({'args': function, 'result': result})

    def __call__(self, function):
        # TODO вызов функции
        def _def_(*args, **kwargs):
            if self.ttl and time.time() - self.timestart > self.ttl:
                self.cache = deque()
            for i in self.cache:
                if i['args'] == (args, kwargs):
                    self.cache.remove(i)
                    self.cache.appendleft(i)
                    return i['result']
            result = function(*args, **kwargs)
            self.put((args, kwargs), result)
            return result
        self.timestart = time.time()
        return _def_
