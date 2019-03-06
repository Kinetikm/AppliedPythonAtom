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
    stack = []
    for i in input_string:
        try:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            elif i == ")":
                if stack.pop() != "(":
                    return False
            elif i == "]":
                if stack.pop() != "[":
                    return False
            elif i == "}":
                if stack.pop() != "{":
                    return False
            else:
                return False
        except KeyError:
            return False
    return True
    raise NotImplementedError
