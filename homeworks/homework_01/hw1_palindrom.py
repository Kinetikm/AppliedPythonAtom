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
    if len(input_string) == 0:
        return True
    for index in range(0, int(len(input_string) / 2) + 1):
        if input_string[index] != input_string[len(input_string) - index - 1]:
            return False
    return True
