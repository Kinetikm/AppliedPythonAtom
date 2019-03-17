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
            return self.get_key() == other

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """
        self.lists = list()
        for _ in range(bucket_num):
            self.lists.append(list())

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        n = self._get_index(self._get_hash(key))
        for elem in self.lists[n]:
            if key == elem.get_key():
                return elem.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        n = self._get_index(self._get_hash(key))
        new = self.Entry(key, value)
        if self.get(key) is None:
            self.lists[n].append(new)
        else:
            n = self._get_index(self._get_hash(key))
            for elem in self.lists[n]:
                if key == elem:
                    elem._value = value
        if len(self) / len(self.lists) > 0.7:
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        n = 0
        for l in self.lists:
            n += len(l)
        return n

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % len(self.lists)

    class Val(object):
        def __init__(self, lists):
            self.i = 0
            self.lists = lists

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < len(self.lists):
                self.i += 1
                return self.lists[self.i - 1].get_value()
            else:
                raise StopIteration

    def values(self):
        # TODO Должен возвращать итератор значений
        spisok = list()
        for l in self.lists:
            spisok += list(l)
        return self.Val(spisok)

    class Key(object):
        def __init__(self, lists):
            self.i = 0
            self.lists = lists

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < len(self.lists):
                self.i += 1
                return self.lists[self.i - 1].get_key()
            else:
                raise StopIteration

    def keys(self):
        # TODO Должен возвращать итератор ключей
        spisok = list()
        for l in self.lists:
            spisok += list(l)
        return self.Key(spisok)

    class Item(object):
        def __init__(self, lists):
            self.i = 0
            self.lists = lists

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < len(self.lists):
                self.i += 1
                t = (
                    self.lists[self.i - 1].get_key(),
                    self.lists[self.i - 1].get_value(),
                )
                return t
            else:
                raise StopIteration

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        spisok = list()
        for l in self.lists:
            spisok += list(l)
        return self.Item(spisok)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        spisok = list()
        for l in self.lists:
            spisok += list(l)
        for l in self.lists:
            l.clear()
        for _ in range(len(self.lists)):
            self.lists.append(list())
        for elem in spisok:
            self.put(elem.get_key(), elem.get_value())

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        s = "buckets: "
        for l in self.lists:
            i = False
            s += "{"
            for elem in l:
                if i:
                    s += " "
                s = s + str(elem.get_key()) + ":" + str(elem.get_value())
                i = True
            s += "} "
        return s

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        spisok = list()
        for l in self.lists:
            spisok += list(l)
        for i in spisok:
            if item == i.get_key():
                return True
