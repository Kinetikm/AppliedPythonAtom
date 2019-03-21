#!/usr/bin/env python
# coding: utf-8
import time


class _LRUCacheDecorator:

    def __init__(self, func, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        self._func = func
        self._ttl = ttl
        self._lrucache = {}
        self._lrudeq = []
        self._maxsize = maxsize

    def __call__(self, arg):
        ret = self._lrucache.get(arg)
        if ret is None or self._ttl is not None and time.time() \
                - ret['create_time'] > self._ttl:
            self._lrucache[arg] = dict(create_time=time.time(),
                                       value=self._func(arg))
        try:
            del self._lrudeq[self._lrudeq.index(arg)]
        except ValueError:
            if self._maxsize <= len(self._lrudeq):
                del self._lrucache[self._lrudeq.pop(0)]
        self._lrudeq.append(arg)
        return self._lrucache[arg]['value']


def LRUCacheDecorator(maxsize, ttl):
    def _caller(func):
        return _LRUCacheDecorator(func, maxsize, ttl)

    return _caller
