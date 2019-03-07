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
    i = 0
    str = input_string
    if (str == ""):
        return True
    else:
        if (str[0] is "}") or (str[0] is ")") or (str[0] is "]"):
            return False
        else:
            while (i < len(str)) and\
                    ((str[i] is "{") or (str[i] is "(") or (str[i] is "[")):
                i = i + 1
            if i != len(str):
                p = str[i-1] + str[i]
                if (p == "[]") or (p == "{}") or (p == "()"):
                    if i == (len(str)-1):
                        Str = str[:i-1]
                    else:
                        Str = str[:i-1] + str[i+1:]
                    return is_bracket_correct(Str)
                else:
                    return False
            else:
                return False
    raise NotImplementedError
