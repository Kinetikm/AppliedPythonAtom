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

        def __str__(self):
            return "[key: {}, value: {}]".format(self._key, self._value)

        def __repr__(self):
            return "[key: {}, value: {}]".format(self._key, self._value)

    class MyIterator:
        def __iter__(self):
            return self

        def __init__(self, table):
            self.__table = table
            self.__bucket_iter = iter(table)
            self.__item_iter = iter(next(self.__bucket_iter))

        def __next__(self):
            try:
                return self._format(next(self.__item_iter))
            except StopIteration:
                while True:
                    self.__item_iter = iter(next(self.__bucket_iter))
                    try:
                        return self._format(next(self.__item_iter))
                    except:
                        pass

        def _format(self, item):
            return item

    class ValuesIterator(MyIterator):
        def _format(self, item):
            return item.get_value()

    class KeysIterator(MyIterator):
        def _format(self, item):
            return item.get_key()

    class ItemsIterator(MyIterator):
        def _format(self, item):
            return (item.get_key(), item.get_value())

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
        try:
            index = self._get_index(self._get_hash(key))
        except:
            return default_value
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == key:
                return entry.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        try:
            index = self._get_index(self._get_hash(key))
        except:
            return None
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == key:
                entry._value = value
                return
        bucket.append(self.Entry(key, value))
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
        return hash_value % self.__reserved

    def values(self):
        # TODO Должен возвращать итератор значений
        return self.ValuesIterator(self.__table)

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return self.KeysIterator(self.__table)

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return self.ItemsIterator(self.__table)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        entryes = []
        for bucket in self.__table:
            entryes = entryes + bucket
        self.__size = 0
        self.__reserved *= 2
        self.__table = [[] for i in range(self.__reserved)]
        for entry in entryes:
            self.put(entry.get_key(), entry.get_value())

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        list_of_items = [item for item in self.items()]
        return "buckets: {}, items: {}".format(self.__table, list_of_items)

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        index = self._get_index(self._get_hash(item))
        bucket = self.__table[index]
        for entry in bucket:
            if entry.get_key() == item:
                return True
        return False
