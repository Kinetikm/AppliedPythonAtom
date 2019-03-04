#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    for i in range(len(input_string)):
        if (input_string[i] == '(' and input_string[- (i + 1)] == ')') or (
                input_string[i] == '[' and input_string[- (i + 1)] == ']') or (
                input_string[i] == '{' and input_string[- (i + 1)] == '}'):
            return True
        else:
            return False

#    '''
#    Метод проверяющий является ли поданная скобочная
#     последовательность правильной (скобки открываются и закрываются)
#     не пересекаются
#    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
#    :return: True or False
#     '''
#    raise NotImplementedError
