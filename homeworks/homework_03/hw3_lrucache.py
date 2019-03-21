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

    def __call__(self, *args, **kwargs):
        if self.cache.get(args) is None or\
                (self.clock and time.time() - self.init_time >= self.clock):
            res = self.func(*args, **kwargs)
            if len(self.cache) == self.max_size:
                found = min(self.cache.items(), key=lambda el: el[1][1])
                del self.cache[found[0]]

            if self.cache.get(args) is None:
                self.cache[args] = [res, time.time()]
            else:
                self.cache[args][1] = time.time()
            return res

        self.cache[args][1] = time.time()
        return self.cache.get(args)[0]


def LRUCacheDecorator(function=None, maxsize=10, ttl=10):
    if function:
        return _LRUCacheDecorator(function, maxsize, ttl)
    else:
        def wrapper(function):
            return _LRUCacheDecorator(function, maxsize, ttl)
        return wrapper
