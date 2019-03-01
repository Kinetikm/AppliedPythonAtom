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
    queue = []
    open_bracket = '{(['
    close_bracket = '})]'
    for char in input_string:
        if char in open_bracket:
            queue.append(char)
        else:
            if len(queue) == 0:
                return False
            if open_bracket.find(queue[-1]) == close_bracket.find(char):
                queue.pop()
            else:
                return False
    return len(queue) == 0
