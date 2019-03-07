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
    brdict = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack = []
    if not isinstance(input_string, str):
        return False
    for ch in input_string:
        if ch in brdict.values():
            stack.append(ch)
        elif ch in brdict:
            if (len(stack) > 0) and (brdict[ch] == stack[-1]):
                stack.pop(-1)
            else:
                return False
    return True
