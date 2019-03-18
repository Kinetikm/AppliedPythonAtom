#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    __CONST_Max_State = 0.75  # Константа - предел заполненности HashMap

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
            return self._key == other.get_key()

        def set_value(self, value):
            # Устанавливает значение
            self._value = value

        def __str__(self):
            # Метод возвращает 'key: {}, value: {}'
            return "Entry [key: {}, value:{}]".format(self.__key, self.__value)

        def __repr__(self):
            # Метод возвращает '{key},{value}'
            return '({},{})'.format(self._key, self._value)

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.__size = bucket_num  # Текущий размер HashMap
        # Структура: cписок списков Entry
        self.__table = [[] for i in range(self.__size)]
        self.__buckets = 0  # Количество заполненных ячеек
        # Процент заполненности таблицы.
        self.__percent = self.__buckets / self.__size

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        ind = self._get_index(self._get_hash(key))
        if ind is None:
            return default_value
        else:
            for item in self.__table[ind]:
                if item.get_key() == key:
                    return item.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        ind = self._get_index(self._get_hash(key))
        if ind is not None:
            fl = False
            for item in self.__table[ind]:
                if item.get_key() == key:
                    item.set_value(value)
                    fl = True
                    break
            if fl is False:
                self.__table[ind].append(self.Entry(key, value))
                self.__buckets += 1
        else:
            print("Invalid key")
        if self.__percent >= self.__CONST_Max_State:
            self._resize()

    def __len__(self):  # Возвращает
        return self.__buckets

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):  # Возвращает индекс по хэшу
        return hash_value % self.__size

    def values(self):  # Итератор значений
        __val = list()
        for bucket in self.__table:
            for _entery in bucket:
                __val.append(_entery.get_value())
        return __val

    def keys(self):  # Итератор ключей
        __keys = list()
        for bucket in self.__table:
            for _entery in bucket:
                __keys.append(_entery.get_key())
        return __keys

    def items(self):  # Итератор пар ключ-значение
        _entery_list = list()
        for bucket in self.__table:
            _entery_list += [(it.get_key(), it.get_value()) for it in bucket]
        return _entery_list

    def _resize(self):  # resize по capacity
        self.__size = int(self.__size * 1.6)
        old_table = self.items()
        self.__table = [[] for i in range(self.__size)]
        for item in old_table:
            self.put(item[0], item[1])

    def __str__(self):  # Вывод
        print("buckets: {}, items: {}".format(self.__buckets, self.items()))

    def __contains__(self, item):  # check: in ?
        for i in self.__table:
            for j in i:
                if j.get_key() == item:
                    return True
        return False
