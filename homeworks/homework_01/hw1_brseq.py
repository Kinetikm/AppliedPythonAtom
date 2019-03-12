#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    tmp1 = []
    len1 = len(input_string)
    flag = 1
    for i in range(len1):
        tmp1.append(input_string[i])

    if len1 % 2 == 1:
        return False
    for i in range(len1 - 1):
        if tmp1[i] == '(':
            if tmp1[i + 1] != ')':
                return False
        if tmp1[i] == '{':
            if tmp1[i + 1] != '}':
                return False
        if tmp1[i] == '[':
            if tmp1[i + 1] != ']':
                return False
    else:
        return True


print(is_bracket_correct('{}()[]'))
