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
            return self._key

        def get_value(self):
            return self._value

        def __eq__(self, other):
            return self._key == other._key
        
        def __repr__(self):
            if self._value == None:
                return f'{self._key}'
            return f'**key: {self._key}, value: {self._value}**\n'

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self._size = 0
        self._hash_bucket = [None] * bucket_num

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        key_hash = self._get_hash(key)
        elem_index = self._get_index(key_hash)
        if (not self._hash_bucket[elem_index]):
            return default_value
        else:
            list_of_elem = self._hash_bucket[elem_index]
            for elem in list_of_elem:
                if (key == elem.get_key()):
                    return elem.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        key_hash = self._get_hash(key)
        elem_index = self._get_index(key_hash)
        elem = self.Entry(key, value)
        if (not self._hash_bucket[elem_index]):
            self._hash_bucket[elem_index] = [elem]
            self._size += 1
        else:
            list_of_elem = self._hash_bucket[elem_index]
            if (elem not in list_of_elem):
                list_of_elem.append(elem)
                self._size += 1
            else:
                for stored_elem in list_of_elem:
                    if elem == stored_elem:
                        stored_elem._value = elem._value
                        break
        if (self._size / len(self._hash_bucket) > 0.75):
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self._size

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self._hash_bucket)

    def values(self):
        # TODO Должен возвращать итератор значений
        return (item[1] for item in self.items())

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return (item[0] for item in self.items())

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return ((entry.get_key(), entry.get_value())
                for bucket in self._hash_bucket if bucket is not None for entry in bucket)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        items = self.items()
        self._size = 0
        self._hash_bucket = len(self._hash_bucket) * 2 * [None]
        for item in items:
            self.put(*item)

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        return f"buckets: {self._hash_bucket}, items: {self.items()}"

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        pos = self._get_index(self._get_hash(item))

        if self._hash_bucket[pos] is None:
            return False
        for entry in self._hash_bucket[pos]:
            if entry._key == item:
                return True
        return False
