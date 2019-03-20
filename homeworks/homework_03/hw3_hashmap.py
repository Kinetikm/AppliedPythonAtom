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
            raise NotImplementedError

        def get_value(self):
            # TODO возвращаем значение
            return self.value
            raise NotImplementedError

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.key == other.key
            raise NotImplementedError

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.buckets = [None] * bucket_num
        self.num_entry = 0
        # raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        if self.buckets[index] is not None:
            for element in self.buckets[index]:
                if element.get_key() == key:
                    return element.get_value()
        return default_value
        raise NotImplementedError

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        hash_key = self._get_hash(key)
        index = self._get_index(hash_key)
        if self.buckets[index] is not None:
            for element in self.buckets[index]:
                if element.get_key() == key:
                    element.value = value
                    return
            self.buckets[index].append(self.Entry(key, value))
            self.num_entry += 1
        else:
            self.buckets[index] = [self.Entry(key, value)]
            self.num_entry += 1
        print(self.__len__())
        if len(self) > 0.75 * len(self.buckets):
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.num_entry
        raise NotImplementedError

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)
        raise NotImplementedError

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.buckets)
        raise NotImplementedError

    def values(self):
        # TODO Должен возвращать итератор значений
        return [item[1] for item in self.items()]
        raise NotImplementedError

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return [item[0] for item in self.items()]
        raise NotImplementedError

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        items = []
        for bucket in self.buckets:
            if bucket is not None:
                for element in bucket:
                    items.append((element.get_key(), element.get_value()))
        return items
        raise NotImplementedError

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
        raise NotImplementedError

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        return (item in self.keys())
        raise NotImplementedError
