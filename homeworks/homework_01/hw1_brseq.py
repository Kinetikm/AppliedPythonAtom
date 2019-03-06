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

    if (input_string == ""):
        return True
    else:
        stack = []
        rever = {')': '(', ']': '[', '}': '{'}

        for s in input_string:
            if s in ['(', '[', '{']:
                stack.append(s)
            if s in [')', ']', '}']:
                if (len(stack) == 0):
                    return False
                if (rever[s] == stack[-1]):
                    stack.pop(-1)
                else:
                    return False

        return len(stack) == 0
