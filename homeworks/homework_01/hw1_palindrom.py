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
    len1 = len(input_string)
    tmp1 = []
    flag = 0
    for i in range(len1):
        tmp1.append(input_string[i])
    for i in range(len1):
        if (tmp1[i - 1] != tmp1[-i]):
            flag = 1

    if (flag == 0):
        return True
    else:
        return False
