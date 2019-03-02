#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    """
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    """
    n = 0
    m = 0
    p = 0
    a = []

    for s in input_string:
        if (s == "}" or s == "]" or s == ")") and len(a) == 0:
            return False
        elif s == "}" and a[-1] == "{":
            a.pop()
        elif s == "}" and a[-1] != "{":
            return False
        elif s == ")" and a[-1] == "(":
            a.pop()
        elif s == ")" and a[-1] != "(":
            return False
        elif s == "]" and a[-1] == "[":
            a.pop()
        elif s == "]" and a[-1] != "[":
            return False
        else:
            a.append(s)

    return True
