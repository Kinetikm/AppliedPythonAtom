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
    stack = list()
    for bracket in input_string:
        if (bracket == '(' or bracket == '{' or bracket == '['):
            stack.append(bracket)
            continue
        if ((bracket == ')' or bracket == '}' or bracket == ']') and
                len(stack) != 0):
            if ((stack[-1] == '(' and bracket == ')') or (stack[-1] ==
                '{' and bracket == '}') or (stack[-1] == '[' and bracket == ']')):
                del stack[-1]
            else:
                print(stack)
                print(bracket)
                return False
    if (stack):
        return False
    else:
        return True

    raise NotImplementedError
