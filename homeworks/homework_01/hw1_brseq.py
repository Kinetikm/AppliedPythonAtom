#!/usr/bin/env python
# coding: utf-8


def pair_bracker(lhs, rhs):
    return lhs + rhs in ['()', '[]', '{}']


def is_bracket_correct(input_string):
        # Метод проверяющий является ли поданная скобочная
        # последовательность правильной (скобки открываются и закрываются)
        # не пересекаются
        # :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
        # :return: True or False
    stack = []
    for i in input_string:

        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if len(stack) == 0:
                return False
            if not pair_bracker(stack.pop(), i):
                return False
        else:
            continue

    if len(stack) == 0:
        return True
    else:
        return False
