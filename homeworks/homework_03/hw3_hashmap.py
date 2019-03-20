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
            return self.key == other.key

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.bucket_num = bucket_num
        self.buckets = [None] * self.bucket_num
        self.lenf = 0

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        i = self._get_index(self._get_hash(key))
        if self.buckets[i] is not None:
            for ent in self.buckets[i]:
                if ent.get_key() == key:
                    return ent.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        i = self._get_index(self._get_hash(key))
        k = 0
        if self.buckets[i] is not None:
            for ent in self.buckets[i]:
                if ent.get_key() == key:
                    ent.value = value
                    k = 1
            if k == 0:
                self.buckets[i].append(self.Entry(key, value))
                self.lenf += 1

        else:
            self.buckets[i] = [self.Entry(key, value)]
            self.lenf += 1
        if (len(self) / len(self.buckets)) > 0.75:
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.lenf

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.buckets)

    def values(self):
        # TODO Должен возвращать итератор значений
        return (item[1] for item in self.items())

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return (item[0] for item in self.items())

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        item = []
        for j in self.buckets:
            if j is not None:
                for i in j:
                    item.append((i.get_key(), i.get_value()))
        return item

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        new_backet = HashMap(bucket_num=len(self.buckets) * 2)
        for item in self.items():
            new_backet.put(item[0], item[1])
        self.bucket = new_backet
        del new_backet

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return 'buckets: {}, items: {}'.format(self.buckets, self.items())

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        return (item in self.keys())
