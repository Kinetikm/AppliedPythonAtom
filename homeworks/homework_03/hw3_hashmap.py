#!/usr/bin/env python
# coding: utf-8


class HashMap:
    """
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    """

    class Entry:
        def __init__(self, key, value):
            """
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            """

            self.key = key
            self.value = value

        def get_key(self):
            # возвращаем ключ
            return self.key

        def get_value(self):
            # возвращаем значение
            return self.value

        def set_value(self, new_value):
            self.value = new_value

        def __eq__(self, other):
            # реализовать функцию сравнения
            return self.key == other.get_key()

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """

        self.capacity = bucket_num
        self.real_size = 0
        self.buckets = [[] for k in range(bucket_num)]

    def get(self, key, default_value=None):
        # метод get, возвращающий значение,
        # если оно присутствует, иначе default_value
        # ищем позицию по хэшкоду ключа
        try:
            pos = self._get_index(self._get_hash(key))

            for it in self.buckets[pos]:
                if it.get_key() == key:
                    return it.get_value()

            return default_value

        except TypeError:
            return

    def put(self, key, value):
        # метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        try:
            pos = self._get_index(self._get_hash(key))
            if key in list(self.keys()):
                for it in self.buckets[pos]:
                    if it.get_key() == key:
                        it.set_value(value)
                    else:
                        self.buckets[pos].append(self.Entry(key, value))
            else:
                self.buckets[pos].append(self.Entry(key, value))
                self.real_size += 1

            # предельное значение
            threshold = 0.75*self.capacity
            if self.real_size == threshold:
                self._resize()

        except TypeError:
            return

    def __len__(self):
        # Возвращает количество Entry в массиве
        return self.real_size

    def _get_hash(self, key):
        #  Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.capacity

    def values(self):
        # Должен возвращать итератор значений
        buf = []
        for bucket in self.buckets:
            buf.extend([it.get_value() for it in bucket])
        return iter(buf)

    def keys(self):
        # Должен возвращать итератор ключей
        buf = []
        for bucket in self.buckets:
            buf.extend([it.get_key() for it in bucket])
        return iter(buf)

    def items(self):
        # Должен возвращать итератор пар ключ и значение (tuples)
        return zip(self.keys(), self.values())

    def _resize(self):
        # Время от времени нужно ресайзить нашу хешмапу
        buf = self.items()

        # сброс параметров
        self.capacity *= 2
        self.real_size = 0
        self.buckets = [[] for k in range(self.capacity)]

        for k, it in buf:
            self.put(k, it)

    def __str__(self):
        # Метод выводит "buckets: {}, items: {}"
        return 'buckets: {}, items: {}'.format(self.buckets,
                                               ', '.join(str(it) for it in self.items()))

    def __contains__(self, item):
        # Метод проверяющий есть ли объект (через in)
        return item in list(self.keys())
