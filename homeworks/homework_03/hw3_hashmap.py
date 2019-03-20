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

        def set_value(self, value):
            self.value = value

        def __eq__(self, other):
            if other.get_key() == self.key:
                return True
            return False

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.bucket_num = bucket_num
        self.list_of_buckets = [None] * bucket_num
        self.length = 0

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        index = self._get_index(self._get_hash(key))
        if self.list_of_buckets[index]:
            list_in_bucket = self.list_of_buckets[index]
            for element in list_in_bucket:
                if element.get_key() == key:
                    return element.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        __index = self._get_index(self._get_hash(key))
        if self.list_of_buckets[__index]:
            __list_in_bucket = self.list_of_buckets[__index]
            for element in __list_in_bucket:
                if element.get_key() == key:
                    element.set_value(value)
                    return
            self.length += 1
            __list_in_bucket.append(self.Entry(key, value))
        else:
            self.length += 1
            self.list_of_buckets[__index] = [self.Entry(key, value)]
        if self.length >= 0.75 * self.bucket_num:
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.length

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.bucket_num

    def values(self):
        # TODO Должен возвращать итератор значений
        return iter([x[1] for x in self.__list_of_items()])

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return iter([x[0] for x in self.__list_of_items()])

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return iter(self.__list_of_items())

    def __list_of_items(self):
        __items = []
        for i in range(len(self.list_of_buckets)):
            if self.list_of_buckets[i]:
                __list_in_bucket = self.list_of_buckets[i]
                for element in __list_in_bucket:
                    __items.append((element.get_key(), element.get_value()))
        return __items

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        __old_bucket_list = self.__list_of_items()
        self.list_of_buckets = [None] * int(self.bucket_num + 1)
        self.bucket_num = int(self.bucket_num + 1)
        self.length = 0
        for element in __old_bucket_list:
            self.put(element[0], element[1])

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        __print_this_list = self.__list_of_items()
        indexes = []
        for i in range(len(self.list_of_buckets)):
            if self.list_of_buckets[i]:
                indexes.append(i)
            else:
                indexes.append(None)

        return str("buckets: {}, items: {}".format(indexes, __print_this_list))

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        if item in [x[0] for x in self.__list_of_items()]:
            return True
        else:
            return False
