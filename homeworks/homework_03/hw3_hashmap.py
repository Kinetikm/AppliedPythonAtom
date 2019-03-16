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
            self.__key = key
            self.__value = value

        def get_key(self):
            """Возвращает ключ"""
            return self.__key

        def get_value(self):
            """Возвращает значение"""
            return self.__value

        def set_value(self, value):
            """Устанавливает значение"""
            self.__value = value

        def __eq__(self, other):
            """Функция сравнения"""
            if self.get_key() == other.get_key():
                return True
            return False

        def __str__(self):
            """Метод выводит 'key: {}, value: {}'"""
            return "Entry [key: {}, value:{}]".format(self.__key, self.__value)

        def __repr__(self):
            """Метод выводит 'key: {}, value: {}'"""
            return "Entry [key: {}, value:{}]".format(self.__key, self.__value)

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """
        self._buckets = list()
        self._size = bucket_num
        self._entries = 0
        for _ in range(self._size):
            self._buckets.append(list())

    def get(self, key, default_value=None):
        """
        Возвращает значение по ключу
        если оно присутствует, иначе default_value
        """
        # расчёт хеша и индекса
        key_hash = self._get_hash(key)
        pos = self._get_index(key_hash)

        # если выбранный чанк содержит данные ищем по нему
        for item in self._buckets[pos]:
            if item.get_key() == key:
                return item.get_value()

        return default_value

    def put(self, key, value):
        """
        Кладет значение по ключу
        в случае, если ключ уже присутствует он его заменяет
        """
        # расчёт хеша и индекса
        key_hash = self._get_hash(key)
        pos = self._get_index(key_hash)

        # поиск уже существущего ключа по чанку
        for item in self._buckets[pos]:
            if item.get_key() == key:
                item.set_value(value)
                return None

        # добавление новой записи
        self._buckets[pos].append(self.Entry(key, value))
        self._entries += 1

        # resize хеш таблицы при полном заполнении
        if self._entries >= self._size:
            self._resize()

    def __len__(self):
        """Возвращает количество Entry в массиве"""
        return self._entries

    @staticmethod
    def _get_hash(key):
        """Возвращает хеш от ключа"""
        return hash(key)

    def _get_index(self, hash_value):
        """По значению хеша возвращает индекс элемента в массиве"""
        return hash_value % self._size

    def values(self):
        """Возвращает итератор значений"""
        return [item[1] for item in self.items()]

    def keys(self):
        """Возвращает итератор ключей"""
        return [item[0] for item in self.items()]

    def items(self):
        """Возвращает итератор пар ключ и значение (tuples)"""
        items = []
        for bucket in self._buckets:
            for item in bucket:
                items.append((item.get_key(), item.get_value()))
        return items

    def _resize(self):
        """Измененяет размер хэш таблицы"""
        # получаем все элементы
        items = self.items()

        # увеличиваем размерность в 2 раза
        self._size *= 2
        self._buckets = list()
        for _ in range(self._size):
            self._buckets.append(list())
        self._entries = 0

        # перераспределяем содержимое buckets
        for item in items:
            self.put(item[0], item[1])

    def __str__(self):
        """Метод выводит 'buckets: {}, items: {}'"""
        return "buckets: {}, items: {}".format(self._buckets, self.items())

    def __contains__(self, item):
        """Метод проверяющий есть ли объект (через in)"""
        # расчёт хеша и индекса
        key_hash = self._get_hash(item)
        pos = self._get_index(key_hash)

        # поиск по чанку
        for b_item in self._buckets[pos]:
            if b_item.get_key() == item:
                return True
        return False
