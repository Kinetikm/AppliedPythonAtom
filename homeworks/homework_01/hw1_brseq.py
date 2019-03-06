#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    
    a = '()'
    b = '[]'
    c = '{}'
    s = input_string
    for i in range(len(input_string)):
        s = s.replace(a,'')
        s = s.replace(b,'')
        s = s.replace(c,'')
    if s == '':
        return True
    else:
        return False
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    raise NotImplementedError
