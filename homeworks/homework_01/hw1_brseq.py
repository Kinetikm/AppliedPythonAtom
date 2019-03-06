#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    #
    # Метод проверяющий является ли поданная скобочная
    #  последовательность правильной (скобки открываются и закрываются)
    #  не пересекаются
    # :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    # :return: True or False
    return '()' in input_string and '[]' in input_string and '{}' in input_string

#
# print(is_bracket_correct(input('Input string of brackets: ')))
