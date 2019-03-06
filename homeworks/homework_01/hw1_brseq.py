#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    list_bracket = []
    for i in input_string:
        if i == "(" or i == "[" or i == "{":
            list_bracket.append(i)
        elif len(list_bracket) == 0:
            return False
        elif i == ")":
            if list_bracket.pop() != "(":
                return False
        elif i == "]":
            if list_bracket.pop() != "[":
                return False
        elif i == "}":
            if list_bracket.pop() != "{":
                return False
        else:
            return False
    return list_bracket == 0
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
