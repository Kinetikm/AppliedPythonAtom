#!/usr/bin/env python
# coding: utf-8

import time


class _LRUCacheDecorator:

    def __init__(self, function, maxsize=10, ttl=10):
        self.cache = {}
        self.init_time = time.time()
        self.clock = ttl
        self.max_size = maxsize
        self.func = function
        self.last = None

    def __call__(self, *args, **kwargs):
        print(self.cache)
        if self.clock is not None and time.time() - self.init_time >= self.clock:
            self.cache = {}
        if self.cache.get(args) is None:
            res = self.func(*args, **kwargs)
            if len(self.cache) == self.max_size:
                del self.cache[self.last]
            self.last = args
            self.cache[args] = res
            return res
        return self.cache.get(args)


def LRUCacheDecorator(function=None, maxsize=10, ttl=10):
    if function:
        return _LRUCacheDecorator(function, maxsize, ttl)
    else:
        def wrapper(function):
            return _LRUCacheDecorator(function, maxsize, ttl)
        return wrapper
