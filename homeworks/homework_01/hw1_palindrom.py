#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    a = input_string
    b = a[::-1]
    if a == b:
        return True
    else:
        return False
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    raise NotImplementedError
