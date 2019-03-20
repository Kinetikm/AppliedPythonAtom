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
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.current_size = 0
        self.ttl = ttl
        self.maxsize = maxsize
        self.cache = OrderedDict()

    def __call__(self, function):
        # TODO вызов функции
        def decorator(*args, **kwargs):
            item_in_cache = self.cache.get(args)
            if item_in_cache and (
                    not self.ttl or time.time() -
                    item_in_cache[1] <= self.ttl):
                self.cache.pop(args)
                self.cache[args] = (item_in_cache[0], time.time())
                return item_in_cache[0]
            item_to_return = function(*args, **kwargs)
            if self.current_size >= self.maxsize:
                self.cache.popitem(last=False)
            else:
                self.current_size += 1
            self.cache[args] = (item_to_return, time.time())
            return item_to_return

        return decorator
