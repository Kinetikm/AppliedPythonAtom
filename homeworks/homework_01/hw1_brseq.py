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
    if not type(input_string) == str:
        return False
    openBracetsStack = []
    for chr in input_string:
        if (chr not in set('({[)}]')):
            continue
        if (chr in set('({[')):
            openBracetsStack.append(chr)
            continue
        if len(openBracetsStack) == 0:
            return False
        openingBracket = openBracetsStack.pop()
        if (not (
                (openingBracket == '(' and chr == ')') or
                (openingBracket == '[' and chr == ']') or
                (openingBracket == '{' and chr == '}')
                )):
            return False
    if len(openBracetsStack) != 0:
        return False
    return True
