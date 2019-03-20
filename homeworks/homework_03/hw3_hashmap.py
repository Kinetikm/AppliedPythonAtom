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
            return self.value == other

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.size = bucket_num
        self.map = [None] * self.size

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        temp_hash = self._get_hash(key)
        key_hash = self._get_index(temp_hash)

        if self.map[key_hash] is not None:
            for entry in self.map[key_hash]:
                if entry.get_key() == key:
                    return entry.get_value()

        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        temp_hash = self._get_hash(key)
        key_hash = self._get_index(temp_hash)
        key_value = self.Entry(key, value)

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
        else:
            for entry in self.map[key_hash]:
                if entry.get_key() == key:
                    entry.value = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def __len__(self):
        # TODO Возвращает количество Entry в массиве

        counter = 0
        for entry in self.map:
            if entry is not None:
                if len(entry) > 1:
                    for i in entry:
                        counter += 1
                else:
                    counter += 1
        return counter

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)

        return hash_value

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.size

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
        # return 'buckets: {}, items: {}'.format(self.size, self.__len__())
    # return '(buckets: {}, items: {})'.format(self.x, self.y)
        raise NotImplementedError

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        raise NotImplementedError


# a = HashMap()
# a.put('bob', 4)
# a.put('a', 3)
# a.put('bbo', 2)
# a.put('zuy', 19)
# a.put('a', 3)
#
# print(a.__len__())
#
# print(a)