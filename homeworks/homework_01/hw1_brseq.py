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
    if len(input_string) % 2:
        return False
    else:
        s = input_string
        for i in range(int(len(input_string) / 2)):
            a = s.replace('{}', '')
            b = a.replace('()', '')
            s = b.replace('[]', '')
        if s == '':
            return True
        else:
            return False
    raise NotImplementedError
