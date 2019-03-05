#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    length = len(input_string)
    flag = True
    for i in range(0, length // 2):
        if input_string[i] != input_string[length - i - 1]:
            flag = False
            break
    return flag
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
    # raise NotImplementedError
