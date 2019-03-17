#!/usr/bin/env python
# coding: utf-8


from collections import OrderedDict
from time import time


def ms_cur_time():
    return int(round(time() * 1000))


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        """
        Инициализация декоратора
         https://www.geeksforgeeks.org/class-as-decorator-in-python/

        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        """
        self.size = 0
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache_data = OrderedDict()

    def __call__(self, func):
        """Вызов функции"""

        def wrapper(*args, **kwargs):
            # проверяем кэш на наличие такого запроса и то что он еще жив
            cached = self.cache_data.get(args)
            if cached and \
                    (self.ttl is None or ms_cur_time() - cached[1] <= self.ttl):
                # обновление информации
                self.cache_data[args] = (cached[0], ms_cur_time())
                # перемешение вверх
                self.cache_data.move_to_end(args, last=False)
                return cached[0]

            # записи в кэше нет или устарела, вычисляем
            result = func(*args, **kwargs)

            # вытесняем последнюю запись если кэш заполнен
            if self.size >= self.maxsize:
                self.cache_data.popitem(last=True)
            else:
                self.size += 1
            self.cache_data[args] = (result, ms_cur_time())

            return result

        return wrapper
