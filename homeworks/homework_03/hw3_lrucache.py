#!/usr/bin/env python
# coding: utf-8
import time
from collections import OrderedDict


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        self.maxsize = maxsize
        self.ttl = ttl
        self.size = 0
        self.cached = OrderedDict()
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            cached = self.cached.get(args)
            if cached and \
                    (self.ttl is None or int(round(time.time() * 1000)) - cached[1] <= self.ttl):
                self.cached[args] = (cached[0], int(round(time.time() * 1000)))
                self.cached.move_to_end(args, last=False)
                return cached[0]
            result = func(*args, **kwargs)
            if self.size >= self.maxsize:
                self.cached.popitem(last=True)
            else:
                self.size += 1
            self.cached[args] = (result, int(round(time.time() * 1000)))
            return result

        return wrapper
