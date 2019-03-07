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
    count = []
    for char in input_string:
        if char == "{" or char == "(" or char == "[":
            count.append(char)
        else:
            if len(count) == 0:
                return False
            val = count.pop()
            if char == "}" and val != "{":
                return False
            if char == "]" and val != "[":
                return False
            if char == ")" and val != "(":
                return False
    if len(count) == 0:
        return True
    else:
        return False
