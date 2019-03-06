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
    temp = ['[]', '{}', '()']
    ind = input_string.find
    while (True):
        dlina = len(input_string)
        for skob in temp:
            input_string = input_string.replace(skob, '')
        if dlina == len(input_string):
            break
    if input_string == '':
        return True
    else:
        return False
