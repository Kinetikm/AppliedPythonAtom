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
    while "()" in input_string or "{}" in input_string or "[]" in input_string:
        input_string = input_string.replace("()", '')
        input_string = input_string.replace("[]", '')
        input_string = input_string.replace("{}", '')
    if len(input_string) != 0:
        return False
    else:
        return True
