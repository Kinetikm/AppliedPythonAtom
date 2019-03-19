#!/usr/bin/env python
# coding: utf-8
from timeit import default_timer as timer


class LRUCacheDecorator:
    def __init__(self, maxsize, ttl):
        """
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        """
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.max = maxsize
        self.t = ttl
        self.value = dict()
        self.time = dict()
        self.lists = list()

    def __call__(self, f):
        # TODO вызов функции
        def _dec(*args, **kwargs):
            s = list()
            st = ""
            for arg in args:
                s.append(arg)
            for _, value in kwargs.items():
                s.append(value)
            for elem in s:
                st += str(elem)
            hashs = hash(st)
            fhashs = hash(f)
            allhashs = str(fhashs) + str(hashs)

            if allhashs not in self.value:
                self.value[allhashs] = f(*args, **kwargs)
                self.time[allhashs] = timer()
                self.lists.append(allhashs)
            elif self.t is None:
                pass
            elif timer() - self.time[allhashs] > self.t:
                self.value[allhashs] = f(*args, **kwargs)
                self.time[allhashs] = timer()

            if self.max is None:
                pass
            elif len(self.lists) > self.max:
                ex = self.lists[0]
                self.lists.remove(ex)
                self.value.pop(ex)
                self.time.pop(ex)
            self.lists.remove(allhashs)
            self.lists.append(allhashs)
            return self.value[allhashs]

        return _dec
