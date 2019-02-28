#!/usr/bin/env python


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    queue = []
    n = len(input_string)
    opn = '{[('
    cls = '}])'
    for i in range(n):
        if input_string[i] in opn:
            queue.append(input_string[i])
        else:
            if len(queue) == 0:
                return False
            if opn.find(queue[-1]) != cls.find(input_string[i]):
                return False
            queue.pop(-1)
    return len(queue) == 0
