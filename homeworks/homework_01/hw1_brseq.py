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
    counter_round = 0
    counter_square = 0
    counter_fancy = 0

    for i in input_string:

        if i == '(':
            counter_round += 1
        elif i == ')':
            counter_round -= 1
        if counter_round < 0:
            return False

        if i == '[':
            counter_square += 1
        elif i == ']':
            counter_square -= 1
        if counter_square < 0:
            return False

        if i == '{':
            counter_fancy += 1
        elif i == '}':
            counter_fancy -= 1
        if counter_fancy < 0:
            return False

    print(counter_round, counter_square, counter_fancy)

    return counter_round == 0 and\
           counter_fancy == 0 and\
           counter_square == 0
    raise NotImplementedError



