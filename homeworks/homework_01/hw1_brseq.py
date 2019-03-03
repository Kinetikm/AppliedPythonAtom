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
    if len(input_string) % 2 != 0:
        return False
    i = 0
    while i < len(input_string)-1:
        if input_string[i] == "(":
            if input_string[i+1] == ")":
                i = i + 2
                continue
            else:
                return False
        if input_string[i] == "[":
            if input_string[i+1] == "]":
                i = i + 2
                continue
            else:
                return False
        if input_string[i] == "{":
            if input_string[i+1] == "}":
                i = i + 2
                continue
            else:
                return False
        return False
    return True
