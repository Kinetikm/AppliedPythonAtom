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
    open_brackets = {'{': '}', '(': ')', '[': ']'}
    close_brackets = {c for c in open_brackets.values()}
    for ch in input_string:
        if ch in open_brackets:
            stack.append(open_brackets[ch])
        elif ch in close_brackets:
            if not len(stack) or ch != stack.pop():
                return False
    return True
