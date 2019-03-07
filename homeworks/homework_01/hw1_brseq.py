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

    k = 0
    a = input_string
    if len(a) != 0:
        if a[0] == ")" or a[0] == "]" or a[0] == "}":
            return False
        else:
            while k < len(input_string):
                if a[k] == "(" or a[k] == "[" or a[k] == "{":
                    s = a[k] + a[k + 1]
                    if s == "()" or s == "[]" or s == "{}":
                        k += 2
                    else:
                        return False

    else:
        return True

    raise NotImplementedError
