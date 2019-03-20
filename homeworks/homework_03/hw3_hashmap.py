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
            if self._key == other.get_key():
                return True
            else:
                return False

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.__reserved = bucket_num
        self.__table = [[] for i in range(bucket_num)]
        self.__size = 0
        

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        index = self._get_index(self._get_hash(key))
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == key:
                return entry.get_value
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        index = self._get_index(self._get_hash(key))
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == key:
                entry._value = value
                return
        bucket.append(Entry(key, value))
        self.__size += 1
        if self.__size >= self.__reserved:
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.__size

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.__size

    def values(self):
        # TODO Должен возвращать итератор значений
        raise NotImplementedError

    def keys(self):
        # TODO Должен возвращать итератор ключей
        raise NotImplementedError

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        raise NotImplementedError

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        raise NotImplementedError

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        raise NotImplementedError

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        index = self._get_index(self._get_hash(item.get_key()))
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == item.get_key():
                return True
        return False