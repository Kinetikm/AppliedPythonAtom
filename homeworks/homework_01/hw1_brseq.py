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
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for char in input_string:
        if char == "{":
            sum1 += 1
        if char == "}":
            sum1 -= 1
        if char == "[":
            sum2 += 1
        if char == "]":
            sum2 -= 1
        if char == "(":
            sum3 += 1
        if char == ")":
            sum3 -= 1
    if sum1 == 0 and sum2 == 0 and sum3 == 0:
        return True
    else:
        return False

    raise NotImplementedError
