#!/usr/bin/env python
# coding: utf-8


class HashMap:
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self._key_ = key
            self._value_ = value

        def get_key(self):
            # TODO возвращаем ключ
            return self._key_

        def get_value(self):
            # TODO возвращаем значение
            return self._value_

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            if self._key_ == other._key_:
                return True
            else:
                return False

    def __init__(self, bucket_num=64):
        self.table = [None] * bucket_num

    def get(self, key, default_value=None):
        num = self._get_index(self._get_hash(key))
        if self.table[num] is not None:
            for item in self.table[num]:
                if item.get_key() == key:
                    return item.get_value()
        return default_value

    def put(self, key, value):
        if not (None in self.table):
            self._resize()
        num = self._get_index(self._get_hash(key))
        if self.table[num] is None:
            self.table[num] = [self.Entry(key, value)]
            return
        for item in self.table[num]:
            if item.get_key() == key:
                item._value_ = value
                return
        self.table[num].append(self.Entry(key, value))

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        sum = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                sum = sum + len(self.table[i])
        return sum

    def _get_hash(self, key):
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.table)

    def values(self):
        # TODO Должен возвращать итератор значений
        buffer = []
        for item in self.table:
            if item is not None:
                for i in item:
                    buffer.append(i.get_value())
        return buffer

    def keys(self):
        # TODO Должен возвращать итератор ключей
        buffer = []
        for item in self.table:
            if item is not None:
                for i in item:
                    buffer.append(i.get_key())
        return buffer

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        buffer = []
        for item in self.table:
            if item is not None:
                for i in item:
                    buffer.append((i.get_key(), i.get_value()))
        return buffer

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        items = self.items()
        self.table = [None] * 2 * len(self.table)
        for item in items:
            self.put(item[0], item[1])

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return "buckets: {}, items: {}".format(self.table, self.items())

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        for itemB in self.table:
            if itemB is not None:
                for i in itemB:
                    if i._key_ == item:
                        return True
        return False
