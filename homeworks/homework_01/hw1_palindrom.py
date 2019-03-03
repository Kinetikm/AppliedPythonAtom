#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    length = len(input_string)
    return input_string[length // 2:] == \
        input_string[:length // 2 + length % 2][::-1]
