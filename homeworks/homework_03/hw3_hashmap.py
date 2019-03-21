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
            self._key = key
            self._value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self._key

        def get_value(self):
            # TODO возвращаем значение
            return self._value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            if self.__class__ == other.__class__:
                if self._key == other._key:
                    # if self._value == other._value:
                    return True
            return False

        def __str__(self):
            return f"{self._key}:{self._value}"

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self._bucket_num = bucket_num
        self._buckets = [[] for _ in range(self._bucket_num)]
        self._size = 0

    def _get_item(self, key, default_value=None):
        bucket = self._buckets[self._get_index(self._get_hash(key))]
        for i in range(len(bucket)):
            if key == bucket[i].get_key():
                return bucket[i]
        return None

    def get(self, key, default_value=None):
        entry = self._get_item(key)
        if entry is None:
            return default_value
        else:
            return entry.get_value()

    def put(self, key, value):
        idx = self._get_index(self._get_hash(key))
        entry = self._get_item(key)
        if entry is None:
            self._buckets[idx].append(self.Entry(key, value))
            self._size += 1
        else:
            entry._value = value

    def __len__(self):
        return self._size

    def _get_hash(self, key):
        return hash(key)

    def _get_index(self, hash_value):
        return hash_value % self._bucket_num

    def values(self):
        return [entry.get_value() for entries in self._buckets for entry in
                entries]

    def keys(self):
        return [entry.get_key() for entries in self._buckets for entry in
                entries]

    def items(self):
        return [(entry.get_key(), entry.get_value()) for entries in
                self._buckets for entry in entries]

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        # TODO да, было бы не плохо
        raise NotImplementedError

    def __str__(self):
        return "buckets: [{}], items: {}".format(
            ', '.join([str(len(bucket)) for bucket in self._buckets]),
            self.items()
        )

    def __contains__(self, item):
        idx = self._get_index(self._get_hash(item))
        return item in (entry.get_key() for entry in self._buckets[idx])
