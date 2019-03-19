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
            return self.key

        def get_value(self):
            return self.value

        def __eq__(self, other):
            return self.key == other.key

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.bucket_num = bucket_num
        self.store = [None] * self.bucket_num
        self.size = 0
        self.occupancy = 0.8

    def get(self, key, default_value=None):
        # метод get, возвращающий значение,
        # если оно присутствует, иначе default_value
        key_hash = self._get_hash(key)
        index = self._get_index(key_hash)
        if not self.store[index]:
            return default_value
        else:
            list_at_index = self.store[index]
            for i in list_at_index:
                if i.key == key:
                    return i.value
            return default_value

    def put(self, key, value):
        # метод put, кладет значение по ключу,
        # в случае, если ключ уже присутствует он его заменяет
        has_key = key in self
        if not has_key:
            try:
                key_hash = self._get_hash(key)
                index = self._get_index(key_hash)
            except TypeError:
                pass
            else:
                if not self.store[index]:
                    self.store[index] = [self.Entry(key, value)]
                    self.size += 1
                else:
                    self.store[index].append(self.Entry(key, value))
                    self.size += 1
        else:
            for lst in self.store:
                if not lst:
                    continue
                for tpl in lst:
                    if tpl.key == key:
                        tpl.value = value
                        break

        if self.size / self.bucket_num > self.occupancy:
            self._resize()

    def __len__(self):
        # Возвращает количество Entry в массиве
        return self.size

    def _get_hash(self, key):
        '''
        Возвращает хеш от ключа,
        по которому он кладется в бакет
        '''
        return hash(key)

    def _get_index(self, hash_value):
        # По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.bucket_num

    def values(self):
        # Должен возвращать итератор значений
        return (item[1] for item in self.items())

    def keys(self):
        # Должен возвращать итератор ключей
        return (item[0] for item in self.items())

    def items(self):
        # Должен возвращать итератор пар ключ и значение (tuples)
        item_list = []
        for lst in self.store:
            if lst:
                for elem in lst:
                    item_list.append((elem.get_key(),
                                      elem.get_value()))

        return (item for item in item_list)

    def _resize(self):
        # Время от времени нужно ресайзить нашу хешмапу
        items = self.items()
        self.bucket_num += self.bucket_num // 2
        self.store = [None] * self.bucket_num
        self.size = 0
        for it in items:
            self.put(*it)

    def __str__(self):
        # Метод выводит "buckets: {}, items: {}"
        return "buckets: {}, items: {}".format(self.store, list(self.items()))

    def __contains__(self, item):
        # Метод проверяющий есть ли объект (через in)
        index = self._get_index(self._get_hash(item))

        if self.store[index]:
            for elem in self.store[index]:
                if item == elem.key:
                    return True

        return False
