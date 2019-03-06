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

    correct = list()
    for i in input_string:
        if i == '(' or i == '[' or i == '{':
            correct.append(i)
        if i == ')':
            if len(correct) != 0:
                if correct[len(correct) - 1] == '(':
                    correct.pop()
                else:
                    return False
            else:
                return False
        if i == ']':
            if len(correct) != 0:
                if correct[len(correct) - 1] == '[':
                    correct.pop()
                else:
                    return False
            else:
                return False
        if i == '}':
            if len(correct) != 0:
                if correct[len(correct) - 1] == '{':
                    correct.pop()
                else:
                    return False
            else:
                return False
    if len(correct) == 0:
        return True
    else:
        return False
