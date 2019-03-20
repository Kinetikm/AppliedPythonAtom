#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self.key

        def get_value(self):
            # TODO возвращаем значение
            return self.value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            equal = self.key == other.key
            return equal

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.buckets = bucket_num * [None]
        self.EntryNumb = 0
        self.occupancy = self.EntryNumb / bucket_num

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        pos = self._get_index(self._get_hash(key))
        if self.buckets[pos] is not None:
            for i in self.buckets[pos]:
                if i.get_key() == key:
                    return i.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        pos = self._get_index(self._get_hash(key))
        if self.buckets[pos] is None:
            self.buckets[pos] = [self.Entry(key, value)]
            self.EntryNumb += 1
        elif self.Entry(key, value) in self.buckets[pos]:
            for i in self.buckets[pos]:
                if i.get_key() == key:
                    i.value = value
        else:
            self.buckets[pos].append(self.Entry(key, value))
            self.EntryNumb += 1
        self.occupancy = self.EntryNumb / len(self.buckets)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.EntryNumb

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.buckets)

    def values(self):
        # TODO Должен возвращать итератор значений
        return [j.value for i in self.buckets if i is not None
                for j in i]

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return [j.key for i in self.buckets if i is not None
                for j in i]

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return [(j.key, j.value) for i in self.buckets
                if i is not None for j in i]

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        self.buckets += (len(self.buckets) // 2) * [None]

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return "buckets: {}, items: {}".format(self.buckets, self.items())

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        return item in self.keys()
